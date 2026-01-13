from fastapi import FastAPI
from fastapi import APIRouter
from .health import router as health_router
app=FastAPI(title="CICD test")

app.include_router(health_router)
@app.get("/")
def Welcome():
    return{"message":"My CICD fastapi is running"}
