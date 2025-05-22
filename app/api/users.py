from fastapi import Depends
from app.core.security import oauth2_scheme

# Adicione isso aos endpoints que precisam de proteção:
# async def get_current_user(token: str = Depends(oauth2_scheme)):

