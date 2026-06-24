from fastapi import FastAPI


app = FastAPI(
    title="Meeting Intelligence Hub"
)


@app.get("/")
def home():
    return {
        "status": "running",
        "project": "Meeting Intelligence Hub"
    }