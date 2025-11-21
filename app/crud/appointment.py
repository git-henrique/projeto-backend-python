from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate


def create_appointment(db: Session, appointment: AppointmentCreate):
    db_obj = Appointment(**appointment.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_appointments(db: Session):
    return db.query(Appointment).all()


def get_appointment(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()


def update_appointment(db: Session, appointment_id: int, update: AppointmentCreate):
    appointment = get_appointment(db, appointment_id)
    if not appointment:
        return None
    
    for key, value in update.model_dump().items():
        setattr(appointment, key, value)

    db.commit()
    db.refresh(appointment)
    return appointment


def delete_appointment(db: Session, appointment_id: int):
    appointment = get_appointment(db, appointment_id)
    if not appointment:
        return None
    
    db.delete(appointment)
    db.commit()
    return True
