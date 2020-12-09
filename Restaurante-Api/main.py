from db.usuario_db import UsuarioInDB
from db.usuario_db import update_usuario, get_usuario
from models.usuario_models import UsuarioIn, UsuarioOut

import datetime

from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()



@api.post("/usuario/autenticacion/")
async def auth_user(user_in: UsuarioIn):
    user_in_db =get_usuario(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=401, detail="Error en la autenticación")
    return {"Autenticado": True}


 
@api.post("/usuario/crear/") 
async def create_user(user_in: UsuarioIn):
    user_in_db=update_usuario(user_in)
    user_out = UsuarioOut(**user_in_db.dict())
    user_new = get_usuario(user_out.username)
    if user_new == None:
        raise HTTPException(status_code=404,detail="El usuario no ha sido creado")
    return {"Creado": True}