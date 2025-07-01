from fastapi import APIRouter
from services.cloud_9.env_manage import (cloud_nine_env_list,
                                          delete_all_envs)


cloud_nine_apis= APIRouter()

@cloud_nine_apis.get('/list_all_env',tags=["Cloud9"])
def list_all_env(region_name: str):
    return cloud_nine_env_list(region_name)

@cloud_nine_apis.delete('/delete_all_env',tags=["Cloud9"])
def delete_all_env(region_name: str):
    return delete_all_envs(region_name)