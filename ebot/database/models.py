from tortoise.fields.data import DatetimeField, IntField
from tortoise.models import Model


class DateTimeStampMixin:
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)


class UserModel(Model, DateTimeStampMixin):
    user_id = IntField(pk=True)
    credits = IntField(default=0)
