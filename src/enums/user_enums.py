from enum import Enum

from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'
    BANNED = 'BANNED'
    DELETED = 'DELETED'
    MARGED = 'MARGED'


class UserError(Enum):
    WRONG_EMAIL = "Email doesn't contain @"


print(Statuses.list())