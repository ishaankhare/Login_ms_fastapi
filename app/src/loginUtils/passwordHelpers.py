from passlib.context import CryptContext
import starlette.status as status
from src.models.UserModels import *
from src.loginUtils.passwordHelpers import *
from src.loginUtils.tokenHelpers import *
from pydantic import BaseModel

from src.sql import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_creds_db(input_creds, db):
    records = db.query(models.users_auth).filter(models.users_auth.username == input_creds.username).first()

    if records is not None:
        if verify_password(input_creds.password, records.password):
            return 'Logged in'
        else:
            return 'Incorrect Password'
    else:
        return 'User not registered'


def check_creds(input_creds, fake_users_db):

    if input_creds.username in fake_users_db.keys():
        if verify_password(input_creds.password, fake_users_db[input_creds.username]['password']):
            return 'Logged in'
        else:
            return 'Incorrect Password'
    else:
        return 'User not registered'

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def encrypt_password(password):
    return pwd_context.hash(password)