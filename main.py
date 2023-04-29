from sqlalchemy.orm import Session

from src.loginUtils.passwordHelpers import *
from src.loginUtils.tokenHelpers import *
from src.sql import models
from src.sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

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

# app.include_router(usersroute)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def home():
    return {"message": "Hello World to sign-in app"}


@app.post("/sign-in/")
async def signIn(signInInfo: signInBody, response: Response):
    if check_creds(signInInfo, fake_users_db) == 'Logged in':
        response.delete_cookie(key="signInToken")
        response.delete_cookie(key="CurrentClient")
        token = create_access_token(signInInfo.username)
        response = RedirectResponse(f"http://127.0.0.1:8001/user/", status_code=status.HTTP_302_FOUND)
        response.set_cookie(key="signInToken", value=token)
        response.set_cookie(key="CurrentClient", value=signInInfo.username)
        return response
    else:
        return "Incorrect credentials"


@app.get("/sign-out/")
async def signOut(response: Response):
    response.delete_cookie(key="signInToken")
    response.delete_cookie(key="CurrentClient")
    return "Cookies deleted from the client"


@app.post("/sign-in-db/")
async def signIn(signInInfo: signInBody, response: Response, db: Session = Depends(get_db)):
    if check_creds_db(signInInfo, db) == 'Logged in':
        response.delete_cookie(key="signInToken")
        response.delete_cookie(key="CurrentClient")
        token = create_access_token(signInInfo.username)
        response = RedirectResponse(f"http://127.0.0.1:8001/user/", status_code=status.HTTP_302_FOUND)
        response.set_cookie(key="signInToken", value=token)
        response.set_cookie(key="CurrentClient", value=signInInfo.username)
        return response
    else:
        return "Incorrect credentials"


