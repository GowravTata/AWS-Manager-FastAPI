import requests
from pdb import set_trace as bp

host = "http://127.0.0.1:8000/api/v1"
url = f"{host}/create_topic"


params= {'instance_state_name':'running','region_name':'us-east-1'}
payload = {
  'region_name':'us-east-1',
  'topic_name':'TrialByGowrav',
  'attributes':{'FifoTopic':'true','DisplayName':'FirstCreatePipe'},
  'tags': {
    'name':'Gowrav'
  }
}
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.post(url=url, json=payload, params=params)
print('Status Code', response.status_code)
print('Rsponse ->', response.text)
