from fastapi import HTTPException, status
from core.metadata import InstanceStates
from core.connector import AWSClient
from core.metadata import Services
from typing import List,Dict
from pdb import set_trace as bp

def instance_list(region_name: str,instance_state_name: str )-> Dict : 
    try:
        client=AWSClient(Services.ElasticCompute, region_name)
        ec2=client.connect()
        filters= {
                    'Name':'instance-state-name',
                    'Values' : [instance_state_name]
                 }
        response = ec2.describe_instances(Filters=[filters] )  # type: ignore
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                    instances.append({
                    'InstanceId': instance.get('InstanceId'),
                    'State': instance['State']['Name'],
                    'InstanceType': instance.get('InstanceType'),
                    'PublicIP': instance.get('PublicIpAddress'),
                    'PrivateIP': instance.get('PrivateIpAddress'),
                    'LaunchTime': str(instance.get('LaunchTime')),
                    'PlatformDetails': instance.get('PlatformDetails'),
                    'Name': instance.get('Tags')[0]['Value']
                })
        if not instances:
             return {'message':"No Records Found"  }
        return {'data':instances}
    except Exception as error:
        raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
             detail=error.args
             )
             
def get_instance_ids(region_name: str, state: str)-> List:
     try:
          all_instances = instance_list(region_name, state)
          instance_ids = [instance['InstanceId'] for instance in all_instances['data']]
          return instance_ids
     except Exception as error:
          raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
             detail=error.args[0]
             )             

def stop_instance(region_name: str,instance_id: str):
    try:
        all_instances = get_instance_ids(region_name, InstanceStates.running)
        client=AWSClient(Services.ElasticCompute, region_name)
        ec2 = client.connect()
        if instance_id not in all_instances:
             raise HTTPException(status_code=404, detail="Invalid Instance ID")
        response = ec2.stop_instances( # type: ignore
             InstanceIds=[
                  instance_id
             ]
        )
        return {'Message': f'Successfully stopped Instance : {instance_id}'}
    except Exception as error:
        raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
             detail=error.args[0]
             )
    
    
def terminate_all_instances(region_name:str, state: str)->Dict:
     try:
          all_instances = get_instance_ids(region_name,state)
          client=AWSClient(Services.ElasticCompute, region_name)
          ec2 =  client.connect()
          message = {'message':[]}
          for instance in all_instances:
               response = ec2.terminate_instances( # type: ignore
                         InstanceIds=[
                              instance,
                         ]
                    )
               if response:
                    message['message'].append(response['TerminatingInstances'][0]['InstanceId'])
          return message
     except Exception as error:
          raise HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
               detail=error.args[0]
          )