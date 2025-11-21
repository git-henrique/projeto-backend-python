from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime, nullable=False)
    client_id = Column(Integer, ForeignKey("users.id"))
    provider_id = Column(Integer, ForeignKey("users.id"))

    __table_args__ = (UniqueConstraint("provider_id", "date_time", name="unique_provider_schedule"),)