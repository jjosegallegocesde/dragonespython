from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Aliado(Base):
    __tablename__ ='aliados'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres= Column(String(50))
    ubicacion=Column(String(70))
    aporteMonetario=Column(Float)

class Dragon(Base):
    __tablename__='dragones'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    altura=Column(Float)
    numeroVictorias=Column(Integer)


class Jinete(Base):
    __tablename__='jinetes'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    fechaMontura=Column(Date)