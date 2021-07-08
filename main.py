from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi import HTTPException, Header

#openssl rand -hex 32
SECRET_KEY = "dfd7e43879cfbfd86af11ecc8fb0f591727ef127ce1511b1aa7dd9dde323e8a0"
ALGORITHM = "HS256"
HASHPASS = '$2b$12$caYALfS5RqBR2Z03USfh6OWaL1.Gx7F0U82Z8Y.7VnJQ.jgN/XMhu'

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_token_auth_header(authorization):

    if authorization is None:
        raise HTTPException(
            status_code=401, 
            detail='Unauthorized, no authorization found')
    elif authorization.split()[0].lower() != "bearer":
        raise HTTPException(
            status_code=401, 
            detail='Authorization header must start with Bearer')
    elif len(authorization.split()) == 1:
        raise HTTPException(
            status_code=401, 
            detail='Authorization token not found')
    elif len(authorization.split()) > 2:
        raise HTTPException(
            status_code=401, 
            detail='Authorization header be Bearer token')
    else:
        token = authorization.split()[1]
    return token


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


@app.get("/items/")
async def read_items(Authorization: str = Header(None)):
    token = get_token_auth_header(Authorization)
    if verify_password(token, HASHPASS):
        print('verify')
    else:
        print('unauthorized')
    print(token)
    return {"token": token}


if __name__ == '__main__':
    enc = jwt.encode({'user':'dummy'}, SECRET_KEY, algorithm=ALGORITHM)
    print(f'enc {enc}')
    dec = jwt.decode(enc, SECRET_KEY, algorithms=[ALGORITHM])
    print(f'dec {dec}')

    try:
        dec = jwt.decode('faildecode', SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(
            status_code=401, 
            detail='Unable to parse authentication token')
    print(f'fail decode dec {dec}')