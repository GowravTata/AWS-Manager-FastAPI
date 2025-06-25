from fastapi import APIRouter
from services.health.ping import ping_check

health_check_apis = APIRouter()

@health_check_apis.get("/health_check", tags=["Health"])
async def health_check():
    return ping_check()