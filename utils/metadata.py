from enum import Enum
from pydantic import BaseModel
from typing import Optional

tags_metadata=[
    {
        "name":"Health",
        "description":"APIs related to Health"
    },
    {
        "name":"EC2",
        "description":"APIs related to EC2"
    },
    {
        "name":"SNS",
        "description":"APIs related to SNS"
    }
]


class Services(str,Enum):
    ElasticCompute="ec2"
    SNS="sns"

class InstanceStates(str,Enum):
    running =  'running'
    pending= 'pending'
    shutting_down = 'shutting_down'
    terminated = 'terminated'
    stopping='stopping'
    stopped='stopped'
    
class SNSCreateTopicAttributes(BaseModel):
    # DeliveryPolicy: str='true'
    DisplayName: str
    FifoTopic: str='true'
    
    
    
class CreateTopic(BaseModel):
    region_name:str
    topic_name:str
    attributes: SNSCreateTopicAttributes
    tags:dict