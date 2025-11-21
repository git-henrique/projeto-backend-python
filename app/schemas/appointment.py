from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    date_time: datetime
    client_id: int
    provider_id: int

    model_config = {"from_attributes": True}


class Appointment(AppointmentCreate):
    id: int
