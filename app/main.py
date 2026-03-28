from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
from s3 import listar_archivos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 POST → crear usuario
@app.post("/usuarios")
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        edad=usuario.edad
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {
        "mensaje": "Usuario creado correctamente",
        "usuario_id": nuevo_usuario.id
    }

# 🔹 GET → listar archivos S3
@app.get("/archivos")
def obtener_archivos():
    archivos = listar_archivos()
    return {
        "bucket_files": archivos
    }