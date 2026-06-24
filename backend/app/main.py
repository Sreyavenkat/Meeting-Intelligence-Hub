from fastapi import FastAPI

from app.database import engine, Base
from app.models import meeting
from app.routes import upload


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Meeting Intelligence Hub"
)


app.include_router(
    upload.router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Meeting Intelligence Hub API running"
    }