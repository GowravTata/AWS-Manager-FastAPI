from fastapi import APIRouter
from utils.metadata import CreateTopic
from services.sns.handler import create_sns_topic
from pdb import set_trace as bp


sns_apis= APIRouter()

@sns_apis.post('/create_topic',tags=['SNS'])
def create_topic(json_data: CreateTopic):
    payload = json_data.dict()
    return create_sns_topic(payload)