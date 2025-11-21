from fastapi import FastAPI
from app.database import engine, Base
from app.routers import appointment
from app.models import user, appointment as appointment_model

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Agendamentos")

@app.get("/")
def root():
    return {"message":"API funcionando!"}
app.include_router(appointment.router, prefix="/appointments", tags=["Agendamentos"])