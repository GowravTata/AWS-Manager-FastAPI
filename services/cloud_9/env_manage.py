from fastapi import HTTPException, status
from utils.connector import AWSClient
from utils.metadata import Services
from pdb import set_trace as bp


def cloud_nine_env_list(region_name: str='us-east-1')-> dict:
    """
    This function tries to get the Environments present for 
    cloud9
    region_name: name of the region where cloud9 is running
    """
    try:
        client=AWSClient(Services.CloudNine, region_name)
        cloud_nine=client.connect()
        response=cloud_nine.list_environments( # type: ignore
            maxResults=25
        )
        env_ids = response.get('environmentIds')
        return {'env_ids':env_ids}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error.args
        )
    
def delete_all_envs(region_name: str='us-east-1')-> dict:
    """
    This function deletes all the Cloud9 envs present in a 
    region
    region_name: name of the region where cloud9 is running
    """
    try:
        environmentIds = cloud_nine_env_list(region_name)
        client=AWSClient(Services.CloudNine, region_name)
        cloud_nine=client.connect()
        for environmentId in environmentIds['env_ids']:
            response=cloud_nine.delete_environment( # type: ignore
                environmentId=environmentId
            )
        return {'env_ids':f'Successfully deleted Env Ids {environmentIds}'}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error.args
        )
