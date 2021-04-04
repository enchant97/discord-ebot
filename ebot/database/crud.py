from datetime import timedelta
from typing import Tuple

from tortoise import timezone

from ..config import get_settings
from .models import UserModel


async def get_user(user_id: int) -> UserModel:
    return (
        await UserModel.get_or_create(
            user_id=user_id))[0]


async def user_credits(user_id: int, new_credits:int = None) -> int:
    user = await get_user(user_id)
    if new_credits is not None:
        user.credits = new_credits
        await user.save()
    return user.credits


async def user_xp_get(user_id: int) -> Tuple[float, float, int]:
    """
    get the current users xp,
    max required to get to the next level
    and the current level

        :param user_id: the user id
        :return: the current xp, xp required and current level
    """
    user = await get_user(user_id)
    return user.xp, user.xp_required, user.level


async def user_xp_add(user_id: int, add_xp: float) -> bool:
    """
    add xp to the user and return
    whether the user has leveled up

        :param user_id: the user id
        :param add_xp: xp to add
        :return: whether the user has leveled up
    """
    user = await get_user(user_id)
    if add_xp is not None:
        user.xp += add_xp
        if user.levelup_due:
            user.level += 1
            user.xp = 0
            await user.save()
            return True
        await user.save()
    return False


async def cleanup():
    """
    remove users that haven't been updated in a while,
    save disk-space for servers with large amounts of users
    """
    expire_parts = get_settings().get_expire_time()
    now = timezone.now()

    if expire_parts[1] == "d":
        duration = timedelta(days=expire_parts[0])
    elif expire_parts[1] == "w":
        duration = timedelta(weeks=expire_parts[0])
    elif expire_parts[1] == "m":
        duration = timedelta(days=expire_parts[0] * 12)
    elif expire_parts[1] == "y":
        duration = timedelta(days=expire_parts[0] * 365)
    else:
        raise ValueError("unknown expires type")

    expire_dt = now - duration
    await UserModel.filter(updated_at__lt=expire_dt).delete()
