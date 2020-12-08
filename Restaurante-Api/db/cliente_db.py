from typing import Dict
from pydantic import BaseModel

class ClienteInDB(BaseModel):
    telefono: int
    nombre: str
    direccion: str
    barrio: str
    cedula: str
    cumpleanos: str


database_clientes = {
    "3214567895": ClienteInDB(**{"telefono":"3214567895",
                            "nombre":"Pepe",
                            "direccion":"Calle 12 # 20 - 22",
                            "barrio":"Colombia",
                            "cedula":"456123789",
                            "cumpleanos":"01-Feb-80"
                            }),

    "3007894561": ClienteInDB(**{"telefono":"3007894561",
                            "nombre":"Pepita",
                            "direccion":"Carrera 20 # 15 - 12",
                            "barrio":"Parnaso",
                            "cedula":"1123456789",
                            "cumpleanos":"10-Ene-85"
                            }),
}

def get_cliente(telefono: int):
    if telefono in database_clientes.keys():
        return database_clientes[telefono]
    else:
        return None
        
def update_cliente(cliente_in_db: ClienteInDB):
    database_clientes[cliente_in_db.telefono] = cliente_in_db
    return cliente_in_db

def create_cliente(nuevo_cliente: ClienteInDB):
    database_clientes.append(nuevo_cliente)
    return database_clientes[nuevo_cliente.keys()]