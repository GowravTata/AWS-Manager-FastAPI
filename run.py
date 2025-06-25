from fastapi import FastAPI
from views.health.health_views import health_check_apis
from views.ec_2.ec2_views import ec2_apis
from core.metadata import tags_metadata

app = FastAPI(title="AWS Manager",
    contact={
        "name": "Manage AWS Services",
        "url": "http:localhost:8000",
        "email": "bobby.bob@gmail.com",
    }, 
    openapi_tags=tags_metadata)

app.include_router(prefix="/api/v1", router=health_check_apis)
app.include_router(prefix="/api/v1", router=ec2_apis)
