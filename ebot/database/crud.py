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
