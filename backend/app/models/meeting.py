from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class Meeting(Base):

    __tablename__ = "meetings"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    file_path = Column(
        String,
        nullable=False
    )

    word_count = Column(
        Integer
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )