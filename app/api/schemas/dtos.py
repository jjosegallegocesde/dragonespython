from pydantic import BaseModel,Field
from datetime import date,datetime

class AliadoDTOPeticion(BaseModel):
    nombres:str 
    ubicacion:str 
    aporteMonetario:float
    class Config:
        orm_mode=True


class AliadoDTORespuesta(BaseModel):
    id:int
    nombres:str 
    ubicacion:str 
    aporteMonetario:float
    class Config:
        orm_mode=True

class DragonDTOPeticion(BaseModel):
    nombres:str
    edad:int 
    altura:float
    numeroVictorias:int
    class Config:
        orm_mode=True

class DragonDTORespuesta(BaseModel):
    id:int
    nombres:str
    edad:int 
    altura:float
    numeroVictorias:int
    class Config:
        orm_mode=True

class JineteDTOPeticion(BaseModel):
    nombres:str 
    edad:int 
    fechaMontura:date
    class Config:
        orm_mode=True

class JineteDTORespuesta(BaseModel):
    id:int
    nombres:str 
    edad:int 
    fechaMontura:date
    class Config:
        orm_mode=True