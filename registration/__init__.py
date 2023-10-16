from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime, date

registration_router = APIRouter(prefix='/user', tags=['Polzovatel'])

#validatsiya registratsiyi (toje samoe chto i Body)
class RegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    city: str
    birthday: date
    reg_date: datetime = datetime.now()

#validatsiya vxoda v akkaunt (toje samoe chto i Body)
class LoginModel(BaseModel):
    email: str
    password: str

from registration import registration_api