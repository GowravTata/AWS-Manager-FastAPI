from fastapi import APIRouter

health_check_apis = APIRouter()

async def ping_check():
    return {"msg": "I'm up!"}