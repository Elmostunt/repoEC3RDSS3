from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(150), unique=True, index=True)
    edad = Column(Integer)
    fecha_creacion = Column(TIMESTAMP, server_default=func.now())