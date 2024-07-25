from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.dtos import DragonDTOPeticion,DragonDTORespuesta,JineteDTOPeticion,JineteDTORespuesta, AliadoDTOPeticion, AliadoDTORespuesta
from app.api.models.tablas import Dragon,Jinete,Aliado
from app.database.config import SessionLocal, engine

rutas=APIRouter()

def getDB():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

#ENDPOINTS PARA EL API
@rutas.post("/dragones",response_model=DragonDTORespuesta,summary="Crea un dragon en la BD")
def crearDragon(datosCliente:DragonDTOPeticion,db:Session=Depends(getDB())):
    try:
        dragon=Dragon(
            nombres=datosCliente.nombres,
            edad=datosCliente.edad,
            altura=datosCliente.altura,
            numeroVictorias=datosCliente.numeroVictorias
        )
        db.add(dragon) #orden en bd
        db.commit() #valido la operacion que acabo de realizar
        db.refresh(dragon)
        return dragon
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500,detail="tenemos un problema en el servidor")



@rutas.get("/dragones", response_model=List[DragonDTORespuesta],summary="Servicio que lista todos los dragones en BD")
def buscarDragones(db:Session=Depends(getDB())):
    try:
        dragones=db.query(Dragon).all()
        return dragones
    except Exception as error:
        raise HTTPException(status_code=500,detail="tenemos un problema en el servidor")

@rutas.get("dragones/{id}",response_model=DragonDTORespuesta,summary="servicio para buscar un dragon por id")
def buscarDragonPorId(id:int,db:Session=Depends(getDB())):
    try:
        dragon=db.query(Dragon).get(id)
        return dragon
    except Exception as error:
         raise HTTPException(status_code=500,detail="tenemos un problema en el servidor")

def modificarDragonPorId():
    pass 

def eliminarDragonPorId():
    pass