from enum import Enum
from pydantic import BaseModel

class StopInstancePayload(BaseModel):
    instance_id: str = "i-234122d213"
    region_name: str = "us-east-1"
    
class InstanceStates(str,Enum):
    running =  'running'
    pending= 'pending'
    shutting_down = 'shutting_down'
    terminated = 'terminated'
    stopping='stopping'
    stopped='stopped'

class ListInstance(BaseModel):
    region_name: str
    instance_state_name : InstanceStates