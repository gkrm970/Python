from fastapi import APIRouter,Depends,status,HTTPException
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from ..schemas import TokenData

from .. import schemas,models,database
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..database import get_db
from datetime import datetime,timedelta
pwd_context = CryptContext(schemes=["bcrypt"],deprecated ="auto")
oauth2_scheme =Oauth2PasswordBearer(tokenUrl="login")
router = APIRouter()
# openssl rand -hex 32 --> used to generate secrete key in terminal
SECRETE_KEY = "CHFBHBFHFHB"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTE =20

def generate_token(data :dict):
    to_encode = data.copy()
    expire =datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp":expire})
    encoded_jwt =jwt.encode(to_encode,SECRETE_KEY,ALGORITHM)
    return encoded_jwt

@router.post('/login')
def login(request: schemas.Login,db:Session=Depends(get_db)):
    seller =db.query(models.Seller).filter(models.Seller.username ==request.username).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="username not fount/invalid user")
    if not pwd_context.verify(request.password,seller.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid password')
    #generate token
    access_token = generate_token(
        data ={"sub":seller.username}
    )
    return {"access_token":access_token,"token_typr" : "bearer"}

def get_current_user(token:str=Depends(oauth2_scheme)):
    credential_exception =HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid auth credentials",headers={'www-Authenticate':"Bearer"})
    try:
        payload = jwt.decode(token,SECRETE_KEY,algorithms=[ALGORITHM])
        username:str = payload.get('sub')
        if username is None:
            credential_exception
        token_data =TokenData(username=username)
    except JWTError:
        credential_exception

