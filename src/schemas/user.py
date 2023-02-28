from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserError


class User(BaseModel):
    id: int
    name: int
    email: str
    gender: Genders
    status: Statuses


    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserError.WRONG_EMAIL.value)
    