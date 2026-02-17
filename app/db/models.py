from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.session import Base

class SyncLog(Base):
    __tablename__ = "sync_logs"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(50))
    target = Column(String(50))
    status = Column(String(20))
    message = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
