from db.usuario_db import UsuarioInDB
from db.usuario_db import update_usuario, get_usuario
from models.usuario_models import UsuarioIn, UsuarioOut
from db.cliente_db import ClienteInDB
from db.cliente_db import update_cliente, get_cliente, create_cliente, eliminate_cliente, get_all_clientes
from models.cliente_models import ClienteIn, ClienteOut, ClienteInCreate

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

@api.get("/cliente/consulta/{telefono}")
async def buscar_cliente(telefono: int):
    cliente_in_db = get_cliente(telefono)
    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    cliente_out = ClienteOut(**cliente_in_db.dict())
    return cliente_out   

@api.get("/cliente/lista/")
async def buscar_clientes():
    clientes_in_db = get_all_clientes()
    clientes_out = []
    for cliente in clientes_in_db:
        cliente_out = ClienteOut(**cliente.dict())
        clientes_out.append(cliente_out)
    return clientes_out


@api.post("/cliente/crear/") 

async def crear_cliente(cliente_in: ClienteInCreate):
    cliente_in_db = create_cliente(cliente_in)
    cliente_out = ClienteOut(**cliente_in_db.dict())
    return cliente_out

@api.put("/cliente/update/")
async def upd_cliente(cliente_in: ClienteInCreate):
    cliente_in_db = get_cliente(cliente_in.telefono)
    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    
    cliente_in_db = ClienteInCreate(**cliente_in.dict())

    update_cliente(cliente_in_db)
    
    update_out = ClienteOut(**cliente_in_db.dict())
    return update_out

@api.delete("/cliente/delete/") 

async def delete_cliente(cliente_in: ClienteIn):
    cliente_in_db = get_cliente(cliente_in.telefono)
    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    cliente_out = eliminate_cliente(cliente_in_db)
    return cliente_out