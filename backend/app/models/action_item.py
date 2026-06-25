from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class ActionItem(Base):

    __tablename__ = "action_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    meeting_id = Column(
        Integer,
        ForeignKey("meetings.id")
    )

    responsible_person = Column(
        String
    )

    task = Column(
        String
    )

    deadline = Column(
        String
    )