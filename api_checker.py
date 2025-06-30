import requests,os
import json
from pdb import set_trace as bp

host = "http://127.0.0.1:8000/api/v1"
url = f"{host}/list_instances"


params= {'instance_state_name':'running','region_name':'us-east-1'}
payload = ""
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}


response = requests.get(url=url, headers=headers, data=payload, params=params)
print('Status Code', response.status_code)
print('Rsponse ->', response.text)
