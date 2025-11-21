from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.appointment import Appointment, AppointmentCreate
from app.crud.appointment import (
    create_appointment,
    get_appointments,
    get_appointment,
    update_appointment,
    delete_appointment
)

router = APIRouter(prefix="/appointments", tags=["Agendamentos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Appointment)
def create(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db, appointment)


@router.get("/", response_model=list[Appointment])
def list_all(db: Session = Depends(get_db)):
    return get_appointments(db)


@router.get("/{appointment_id}", response_model=Appointment)
def get_one(appointment_id: int, db: Session = Depends(get_db)):
    ap = get_appointment(db, appointment_id)
    if not ap:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return ap


@router.put("/{appointment_id}", response_model=Appointment)
def update(appointment_id: int, updated: AppointmentCreate, db: Session = Depends(get_db)):
    ap = update_appointment(db, appointment_id, updated)
    if not ap:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return ap


@router.delete("/{appointment_id}")
def delete(appointment_id: int, db: Session = Depends(get_db)):
    ok = delete_appointment(db, appointment_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return {"detail": "Deletado com sucesso"}
