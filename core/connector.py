import boto3
from core.config import Config
conf=Config()

class AWSClient:
    def __init__(self,service_name: str,region_name: str):
        self.service_name=service_name
        self.region_name=region_name

    def connect(self)->object:
        self.client_obj =  boto3.client(
                self.service_name,
                region_name=self.region_name,
                aws_access_key_id=conf.AccesskeyID,
                aws_secret_access_key=conf.SecretAccessKey
            )
        return self.client_obj
        