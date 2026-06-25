from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class Decision(Base):

    __tablename__ = "decisions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    meeting_id = Column(
        Integer,
        ForeignKey("meetings.id")
    )

    decision_text = Column(
        String,
        nullable=False
    )