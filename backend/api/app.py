from fastapi import FastAPI
from api.controllers import main_router

app = FastAPI(
    title="API - Open source project observatory",
    version="0.1.0",
    description="FastAPI/Python - Open source project observatory"
)
app.include_router(main_router)
