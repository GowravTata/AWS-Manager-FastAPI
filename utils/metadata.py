from enum import Enum
from pydantic import BaseModel

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
    },
    {
        "name":"Cloud9",
        "description":"APIs related to Cloud9"
    }
]


class Services(str,Enum):
    ElasticCompute="ec2"
    SNS="sns"
    CloudNine='cloud9'

class InstanceStates(str,Enum):
    running =  'running'
    pending= 'pending'
    shutting_down = 'shutting_down'
    terminated = 'terminated'
    stopping='stopping'
    stopped='stopped'
    
class SNSCreateTopicAttributes(BaseModel):
    DisplayName: str
    FifoTopic: str='true'
    
class CreateTopic(BaseModel):
    region_name:str
    topic_name:str
    attributes: SNSCreateTopicAttributes
    tags:dict