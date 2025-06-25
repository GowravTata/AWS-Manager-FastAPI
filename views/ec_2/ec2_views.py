from fastapi import APIRouter
from services.ec_2.inventory import instance_list, stop_instance
from validators.ec2.instances import Payload
from pdb import set_trace as bp


ec2_apis = APIRouter()

@ec2_apis.get("/list_instances/",tags=["EC2"])
def list_all_instances(
    region_name:str,
    instance_state_name: str
    ):
    return instance_list(region_name, instance_state_name)

@ec2_apis.post("/modify_instance",tags=["EC2"])
def modify_instance(details: Payload)-> dict:
    return stop_instance(details.region_name, details.instance_id)
