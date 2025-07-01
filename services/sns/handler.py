import boto3
from fastapi import HTTPException,status
from utils.connector import AWSClient
from utils.metadata import Services, BaseModel
from pdb import set_trace as bp

def create_sns_topic(json_data: dict)-> dict:
    """
    Function to create SNS Topic with payload
    """
    try:
        region_name =json_data.get('region_name')
        topic_name =json_data.get('topic_name')
        attributes =json_data.get('attributes')
        tags=json_data.get('tags')
        tags_pairs =[{'Key':key,'Value':tags[key]} for key in tags]
        client=AWSClient(Services.SNS, region_name)
        sns=client.connect()
        response = sns.create_topic(
            Name=topic_name,
            Attributes=attributes,
            Tags=tags_pairs
            )
        return {'msg':'Success'}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.args
            )
