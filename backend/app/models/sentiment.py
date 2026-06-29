from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.database import Base


class Sentiment(Base):

    __tablename__ = "sentiments"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    meeting_id = Column(
        Integer,
        ForeignKey("meetings.id")
    )


    text = Column(
        String,
        nullable=False
    )


    speaker = Column(
        String,
        nullable=True
    )


    sentiment = Column(
        String,
        nullable=False
    )


    