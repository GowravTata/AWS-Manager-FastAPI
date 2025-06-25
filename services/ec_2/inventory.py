from validators.ec2.instances import ListInstance
from pydantic import ValidationError
from fastapi import HTTPException, status
from core.connector import AWSClient
from typing import List
from pdb import set_trace as bp

def instance_list(region_name: str,instance_state_name: str)-> List : 
    try:
        ListInstance(region_name=region_name,
                               instance_state_name=instance_state_name)
        client=AWSClient('ec2', region_name)
        ec2=client.connect()
        response = ec2.describe_instances(
             Filters=[
                  {
                       'Name':'instance-state-name',
                       'Values' : [instance_state_name]
                  }
             ]
        )
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
        return instances
    except ValidationError as e:
        raise HTTPException(
             status_code=status.HTTP_400_BAD_REQUEST, 
             detail=e.errors()
             )
    except Exception as error:
        raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
             detail=error.args
             )
    

def stop_instance(region_name: str,instance_id: str):
    try:
        client=AWSClient('ec2', region_name)
        ec2 = client.connect()
        all_instances = instance_list(region_name,'running')
        all_instances = [instance['InstanceId'] for instance in all_instances]
        if instance_id not in all_instances:
             raise HTTPException(status_code=404, detail="Invalid Instance ID")
        response = ec2.stop_instances(
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