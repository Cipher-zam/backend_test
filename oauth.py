from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from JWTToken import verify_token

oauth2_schemas = OAuth2PasswordBearer("login")

def get_current_user(token:str=Depends(oauth2_schemas)):
    credential_exception = HTTPException(status.HTTP_401_UNAUTHORIZED,"Could not validate credentials")
    return verify_token(token, credential_exception)
