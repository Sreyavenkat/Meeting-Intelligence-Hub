from fastapi import FastAPI
from app.routes import upload


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