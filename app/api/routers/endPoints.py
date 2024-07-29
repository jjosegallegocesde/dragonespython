from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.dtos import DragonDTOPeticion,DragonDTORespuesta,JineteDTOPeticion,JineteDTORespuesta, AliadoDTOPeticion, AliadoDTORespuesta
from app.api.models.tablas import Dragon,Jinete,Aliado
from app.database.config import SessionLocal

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
def crearDragon(datosCliente: DragonDTOPeticion, db: Session = Depends(getDB)):
    # Verificar si el jinete existe
    jinete = db.query(Jinete).filter(Jinete.id == datosCliente.fk_jinete).first()
    if not jinete:
        raise HTTPException(status_code=400, detail="El jinete proporcionado no existe")

    try:
        dragon = Dragon(
            nombres=datosCliente.nombres,
            edad=datosCliente.edad,
            altura=datosCliente.altura,
            numeroVictorias=datosCliente.numeroVictorias
        )
        db.add(dragon)  # orden en bd
        db.commit()  # valido la operación que acabo de realizar
        db.refresh(dragon)
        return dragon
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Hubo un problema al crear el dragón en la base de datos. Inténtalo de nuevo más tarde.")



@rutas.get("/dragones", response_model=List[DragonDTORespuesta],summary="Servicio que lista todos los dragones en BD")
def buscarDragones(db:Session=Depends(getDB)):
    try:
        dragones=db.query(Dragon).all()
        return dragones
    except Exception as error:
        raise HTTPException(status_code=500,detail="tenemos un problema en el servidor")

@rutas.get("dragones/{id}",response_model=DragonDTORespuesta,summary="servicio para buscar un dragon por id")
def buscarDragonPorId(id:int,db:Session=Depends(getDB)):
    try:
        dragon=db.query(Dragon).get(id)
        return dragon
    except Exception as error:
         raise HTTPException(status_code=500,detail="tenemos un problema en el servidor")

def modificarDragonPorId():
    pass 

def eliminarDragonPorId():
    pass

@rutas.post("/aliados", response_model=AliadoDTORespuesta, summary="Crea un aliado en la BD")
def crearAliado(datosCliente: AliadoDTOPeticion, db: Session = Depends(getDB)):
    try:
        aliado = Aliado(
            nombres=datosCliente.nombres,
            ubicacion=datosCliente.ubicacion,
            aporteMonetario=datosCliente.aporteMonetario
        )
        db.add(aliado)  # orden en bd
        db.commit()  # valido la operación que acabo de realizar
        db.refresh(aliado)
        return aliado
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="tenemos un problema en el servidor")
    

@rutas.get("/aliados", response_model=List[AliadoDTORespuesta], summary="Servicio que lista todos los aliados en BD")
def buscarAliados(db: Session = Depends(getDB)):
    try:
        aliados = db.query(Aliado).all()
        return aliados
    except Exception as error:
        raise HTTPException(status_code=500, detail="tenemos un problema en el servidor") 



@rutas.post("/jinetes", response_model=JineteDTORespuesta, summary="Crea un jinete en la BD")
def crearJinete(datosCliente: JineteDTOPeticion, db: Session = Depends(getDB)):
    try:
        jinete = Jinete(
            nombres=datosCliente.nombres,
            edad=datosCliente.edad,
            fechaMontura=datosCliente.fechaMontura
        )
        db.add(jinete)  # orden en bd
        db.commit()  # valido la operación que acabo de realizar
        db.refresh(jinete)
        return jinete
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="tenemos un problema en el servidor") 



@rutas.get("/jinetes", response_model=List[JineteDTORespuesta], summary="Servicio que lista todos los jinetes en BD")
def buscarJinetes(db: Session = Depends(getDB)):
    try:
        jinetes = db.query(Jinete).all()
        return jinetes
    except Exception as error:
        raise HTTPException(status_code=500, detail="tenemos un problema en el servidor")  