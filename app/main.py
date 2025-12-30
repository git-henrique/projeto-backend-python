from fastapi import FastAPI
from app.database import engine, Base
from app.routers import appointment
from app.models import user, appointment as appointment_model
from app.routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Agendamentos", debug=True)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message":"API funcionando!"}
app.include_router(appointment.router, prefix="/appointments", tags=["Agendamentos"])