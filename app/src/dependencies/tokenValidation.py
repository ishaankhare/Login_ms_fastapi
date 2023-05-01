from fastapi import Request, HTTPException, Response
from src.loginUtils.tokenHelpers import *

from src.loginUtils.tokenHelpers import validate_token

def get_token(request: Request, response: Response):
    token = request.cookies['signInToken']
    token_answer = request.path_params['user']

    if validate_token(token, token_answer) == 'okay':
        response.headers['user'] = token_answer
        return
    else:
        raise HTTPException(status_code=403, detail="Item not found")