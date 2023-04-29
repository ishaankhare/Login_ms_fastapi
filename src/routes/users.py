from fastapi import FastAPI, Request, APIRouter, Depends, Response
from fastapi.responses import RedirectResponse
import starlette.status as status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.models.UserModels import *
from src.loginUtils.passwordHelpers import *
from jose import JWTError, jwt
from datetime import datetime, timedelta
from src.loginUtils.tokenHelpers import *
from src.dependencies.tokenValidation import *

fake_users_db = {
    "ishaan": {
        "username": "ishaan",
        "password": "$2b$12$pQzMeip75gUYQpYtpAqmge7nRPJi1auvAHUfEqj/ZSiauWd0Qz1gm",
    },
    "vihaan": {
        "username": "vihaan",
        "password": "$2b$12$pQzMeip75gUYQpYtpAqmge7nRPJi1auvAHUfEqj/ZSiauWd0Qz1gm",
    },
}


usersroute = APIRouter(prefix='/users', dependencies=[Depends(get_token)])

@usersroute.get("/{user}/home/")
async def userHome(user, request: Request, response: Response):
    message = f'Welcome {user}'
    print(response.headers)
    json_compatible_item_data = jsonable_encoder(message)
    return JSONResponse(content=json_compatible_item_data)

@usersroute.get("/{user}/friends/")
async def userHome(user):
    message = f'Welcome {user} your friends are::::'

    json_compatible_item_data = jsonable_encoder(message)
    return JSONResponse(content=json_compatible_item_data)

