from fastapi import HTTPException, status
from validators.ec2.instances import InstanceStates
from utils.connector import AWSClient
from utils.metadata import Services
from typing import List,Dict

def instance_list(region_name: str,instance_state_name: str)-> Dict or list: # type: ignore
    """
    This function tries to get the instance list based on region name and
    instance state name
    region_name: Name of the region to which instances are to be fetched
    instance_state_name: Name of the instance state to which instances are to
                            be fetched
    """
    try:
        client=AWSClient(Services.ElasticCompute, region_name)
        ec2=client.connect()
        filters= {
                    'Name':'instance-state-name',
                    'Values' : [instance_state_name]
                 }
        response = ec2.describe_instances(Filters=[filters])   # type: ignore
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                    if Services.CloudNine not in instance.get('Tags')[1]['Value']:
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
             return instances
        return {'data':instances}
    except Exception as error:
          raise HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
               detail=error.args
               )

def get_instance_ids(region_name: str, state: str)-> List:
    """
    Function to get instance ids based on region name and instance state
    region_name: Name of the region to which instances are to be fetched
    state: Name of the instance state to which instances are be fetched
    """
    try:
          all_instances = instance_list(region_name, state)
          if isinstance(all_instances,list):
               return all_instances
          instance_ids = [instance['InstanceId'] for instance in
                            all_instances['data']]
          return instance_ids
    except Exception as error:
          raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
             detail=error.args[0]
             )

def stop_instance(region_name: str,instance_id: str) -> Dict:
    """
    Function to stop instance based on region name and instance id
    region_name: Name of the region of instance to be stopped
    state: ID of the instance to be stopped
    """
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
    """
    Function to terminate instance based on region name and instance state
    region_name: Name of the region of instance to be terminated
    state: Name of the instance state to which instances are be terminated
    """
    try:
          message = {'message':[]}
          all_instances = get_instance_ids(region_name,state)
          if isinstance(all_instances,list):
               return  {'message':f'No Instances in {state} state'}
          client=AWSClient(Services.ElasticCompute, region_name)
          ec2 =  client.connect()
          for instance in all_instances: # type: ignore
               response = ec2.terminate_instances( # type: ignore
                         InstanceIds=[
                              instance,
                         ]
                    )
               if response:
                    message['message'].append(response
                    ['TerminatingInstances'][0]['InstanceId'])
          return message
    except Exception as error:
          raise HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
               detail=error.args[0]
          )