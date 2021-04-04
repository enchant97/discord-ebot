from tortoise.fields.data import DatetimeField, FloatField, IntField
from tortoise.models import Model

from ..config import get_settings


class DateTimeStampMixin:
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)


class UserModel(Model, DateTimeStampMixin):
    user_id = IntField(pk=True)
    credits = IntField(default=0)
    level = IntField(default=0)
    xp = FloatField(default=0)

    @property
    def xp_required(self) -> float:
        """
        total xp required for the next level
        """
        return self.level * get_settings().XP_SCALE

    @property
    def levelup_due(self) -> bool:
        """
        check whether a levelup
        is due (user has enough xp)
        """
        if self.xp >= self.xp_required:
            return True
        return False

    class Meta:
        table = "users"
