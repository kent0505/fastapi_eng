from fastapi import Request, HTTPException, Depends, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated
from enum import Enum
from core.config import settings

import jwt

class Roles(str, Enum):
    admin = "admin"
    user = "user"

def signJWT(
    id: int, 
    role: str, 
    exp: int,
) -> str:
    return jwt.encode(
        {
            "id": id,
            "role": role,
            "exp": exp,
        },
        key=settings.jwt.key,
        algorithm=settings.jwt.algorithm,
    )

class JWTBearer(HTTPBearer):
    def __init__(
        self, 
        role: Roles = Roles.admin,
    ):
        super().__init__(auto_error=True)
        self.role = role

    async def __call__(self, request: Request):
        token: HTTPAuthorizationCredentials = await super().__call__(request)

        if token.scheme != "Bearer":
            raise HTTPException(403, "invalid authentication scheme")

        try:
            payload: dict = jwt.decode(
                jwt=token.credentials,
                key=settings.jwt.key,
                algorithms=[settings.jwt.algorithm],
            )
        except:
            raise HTTPException(403, "auth error")

        if self.role == Roles.user:
            allowed_roles = [Roles.user.value, Roles.admin.value]
        else:
            allowed_roles = [self.role, Roles.admin.value]

        if payload.get("role") not in allowed_roles:
            raise HTTPException(403, "access denied for this role")

        return payload.get("id")

UserDep = Annotated[int, Depends(JWTBearer(role=Roles.user))]

def verify_api_key(api_key: str = Header()):
    if api_key != settings.jwt.api_key:
        raise HTTPException(403, "invalid api key")
