from fastapi import APIRouter, Query
from utils.metadata import InstanceStates
from services.ec_2.inventory import ( instance_list, 
                                     stop_instance, 
                                     terminate_all_instances)
from validators.ec2.instances import StopInstancePayload


ec2_apis = APIRouter()

@ec2_apis.get("/list_instances/",tags=["EC2"])
def list_instances_based_on_region_name_and_instance_state_name(
    region_name:str,
    instance_state_name: InstanceStates = Query(...) 
    ):
    return instance_list(region_name, instance_state_name)

@ec2_apis.post("/stop_instance",tags=["EC2"])
def stop_instance_based_on_region_name_and_instance_id(details: StopInstancePayload)-> dict:
    return stop_instance(details.region_name, details.instance_id)

@ec2_apis.delete("/terminate_instances",tags=["EC2"])
def terminate_instances_based_on_region_name_and_state(region_name: str,
                                     state: InstanceStates = Query(...)):
    return terminate_all_instances(region_name, state)