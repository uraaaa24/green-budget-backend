import os
from fastapi import Depends, HTTPException, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from app.infrastructure.db.models.user import UserModel
import firebase_admin
from firebase_admin import auth, credentials

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "serviceAccountKey.json")
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)


async def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if not cred:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        cred = auth.verify_id_token(cred.credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return cred
