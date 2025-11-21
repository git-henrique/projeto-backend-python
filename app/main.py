from fastapi import FastAPI
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Agendamentos")

@app.get("/")
def root():
    return {"message":"API funcionando!"}