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
def crearDragon():
    pass 

def buscarDragones():
    pass

def buscarDragonPorId():
    pass

def modificarDragonPorId():
    pass 

def elimianrDragonPorId():
    pass