import boto3
import os

AccesskeyID = os.getenv("AccesskeyID")
SecretAccessKey = os.getenv("SecretAccessKey")

class AWSClient:
    def __init__(self,service_name: str,region_name: str):
        self.service_name=service_name
        self.region_name=region_name

    def connect(self)->object:
        self.client_obj =  boto3.client(
                self.service_name,
                region_name=self.region_name,
                aws_access_key_id=AccesskeyID,
                aws_secret_access_key=SecretAccessKey
            )
        return self.client_obj
        