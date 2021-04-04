import logging
from random import randint
from typing import Tuple, Union

from discord import Member, User
from discord.ext import commands
from discord.ext.commands.context import Context

from ..database import crud

logger = logging.getLogger(__name__)


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @property
    def starting_credits(self) -> int:
        return 100

    async def withdraw_credits(
            self,
            member: Union[User, Member], credits_: int) -> Union[int, None]:
        curr_credits = await crud.user_credits(member.id)
        if curr_credits >= credits_:
            curr_credits -= credits_
            await crud.user_credits(member.id, curr_credits)
            logger.info("withdraw %s credits from %s", credits_, member)
            return curr_credits
        else:
            logger.info("withdraw %s credits from %s canceled as \
user does not have enough credits", credits_, member)
            return None

    async def deposit_credits(
            self,
            member: Union[User, Member], credits_: int) -> int:
        curr_credits = await crud.user_credits(member.id)
        curr_credits += credits_
        await crud.user_credits(member.id, curr_credits)
        logger.info("deposit %s credits to %s", credits_, member)
        return curr_credits

    async def reset_credits(self, member: Union[User, Member]):
        await crud.user_credits(member.id, self.starting_credits)
        logger.info("reset %s credits", member)

    @commands.command(aliases=["bal"])
    async def balance(self, ctx: Context):
        """
        Your current balance
        """
        curr_credits = await crud.user_credits(ctx.author.id)
        logger.info(
            "%s requested their balance, currently %s",
            ctx.author,
            curr_credits)
        await ctx.send(
            f"you have {curr_credits} credits",
            reference=ctx.message)


class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def add_xp(self, member: Union[User, Member], xp: float):
        await crud.user_xp_add(member.id, xp)
        logger.info("added %s xp to %s", member, xp)

    @commands.command()
    async def level(self, ctx: Context):
        """
        Your current level stats
        """
        curr_xp = await crud.user_xp_get(ctx.author.id)
        logger.info("%s requested their level, currently %s", ctx.author, curr_xp)
        await ctx.send(
            f"level={curr_xp[2]} xp={round(curr_xp[0], 2)}/{curr_xp[1]}",
            reference=ctx.message)

class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def has_won() -> bool:
        return bool(randint(0, 1))

    @commands.command()
    async def gamble(self, ctx: Context, credits_: int):
        """
        Put credits in, get credits back or lose it
        """
        economy: Economy = self.bot.get_cog('Economy')
        level: Level = self.bot.get_cog("Level")

        if await economy.withdraw_credits(ctx.author, credits_) is None:
            logger.info(
                "%s couldn't gamble as they don't have required credits",
                ctx.author)
            await ctx.send(
                "you don't have the credits to gamble",
                reference=ctx.message)
        else:
            if self.has_won():
                logger.info("%s won the gamble", ctx.author)
                await economy.deposit_credits(ctx.author, int(credits_ * 1.5))
                await level.add_xp(ctx.author, 0.2)
                await ctx.send(
                    "you won the gamble!",
                    reference=ctx.message)
            else:
                logger.info("%s lost the gamble", ctx.author)
                await ctx.send(
                    "you lost the gamble",
                    reference=ctx.message)


class Employment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__base_earn = 10

    @commands.command()
    async def work(self, ctx: Context):
        """
        Go to work and earn credits
        """
        economy: Economy = self.bot.get_cog('Economy')
        level: Level = self.bot.get_cog("Level")

        await economy.deposit_credits(ctx.author, self.__base_earn)
        await level.add_xp(ctx.author, 0.2)
        await ctx.send(
            f"you went to work and earned {self.__base_earn} credits",
            reference=ctx.message)
        logger.info("%s went to work", ctx.author)


def setup(bot):
    bot.add_cog(Economy(bot))
    bot.add_cog(Level(bot))
    bot.add_cog(Gambling(bot))
    bot.add_cog(Employment(bot))
