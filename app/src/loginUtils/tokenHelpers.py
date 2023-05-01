from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'd4e8b608ebf9162e7169478ba053626a8ad0bdfff0bbf193044c3eba314a4ac2'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(subject):
    expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def decode_token(token):
    payload = jwt.decode(
        token, SECRET_KEY, algorithms=ALGORITHM
    )
    return payload

def validate_token(token, user):
    payload = decode_token(token)

    if payload['sub'] == user and datetime.fromtimestamp(payload['exp']) > datetime.now():
        return 'okay'
    else:
        return 'Not authorized or token expired'

