from enum import Enum
tags_metadata=[
    {
        "name":"Health",
        "description":"APIs related to Health"
    },
    {
        "name":"EC2",
        "description":"APIs related to EC2"
    }
]



class Services(str,Enum):
    ElasticCompute="ec2"

class InstanceStates(str,Enum):
    running =  'running'
    pending= 'pending'
    shutting_down = 'shutting_down'
    terminated = 'terminated'
    stopping='stopping'
    stopped='stopped'