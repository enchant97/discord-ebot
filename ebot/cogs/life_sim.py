import logging
from collections import defaultdict
from random import randint
from typing import Union

from discord import Member, User
from discord.ext import commands
from discord.ext.commands.context import Context

logger = logging.getLogger(__name__)


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # TODO use database instead
        self.__credits_by_id = defaultdict(lambda: self.starting_credits)

    @property
    def starting_credits(self) -> int:
        return 100

    async def withdraw_credits(self, member: Union[User, Member], credits_: int) -> Union[int, None]:
        if self.__credits_by_id[member.id] >= credits_:
            self.__credits_by_id[member.id] -= credits_
            logger.info("withdraw %s credits from %s", credits_, member)
            return self.__credits_by_id[member.id]
        else:
            logger.info("withdraw %s credits from %s canceled as\
                user does not have enough credits", credits_, member)
            return None

    async def deposit_credits(self, member: Union[User, Member], credits_: int) -> int:
        logger.info("deposit %s credits to %s", credits_, member)
        self.__credits_by_id[member.id] += credits_
        return self.__credits_by_id[member.id]

    async def reset_credits(self, member: Union[User, Member]):
        self.__credits_by_id[member.id] = self.starting_credits

    @commands.command(help="Your current balance")
    async def balance(self, ctx: Context):
        curr_credits = self.__credits_by_id[ctx.author.id]
        logger.info(
            "%s requested their balance, currently %s",
            ctx.author,
            curr_credits)
        await ctx.send(f"you have {curr_credits} credits")


class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def has_won() -> bool:
        return bool(randint(0, 1))

    @commands.command(help="Put credits in, get credits back or lose it")
    async def gamble(self, ctx: Context, credits_: int):
        economy: Economy = self.bot.get_cog('Economy')

        if await economy.withdraw_credits(ctx.author, credits_) is None:
            logger.info(
                "%s couldn't gamble as they don't have required credits",
                ctx.author)
            await ctx.send("you don't have the credits to gamble")
        else:
            if self.has_won():
                logger.info("%s won the gamble", ctx.author)
                await economy.deposit_credits(ctx.author, int(credits_ * 1.5))
                await ctx.send("you won the gamble!")
            else:
                logger.info("%s lost the gamble", ctx.author)
                await ctx.send("you lost the gamble")


def setup(bot):
    bot.add_cog(Economy(bot))
    bot.add_cog(Gambling(bot))
