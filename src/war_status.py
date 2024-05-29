import requests
import json
from datetime import datetime
import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

#https://helldivers-2.github.io/api/docs/openapi/swagger-ui.html

now = datetime.now()
dt_string = now.strftime("%m%d%Y%H%M%S")
dt_formatted = now.strftime("%m-%d-%Y- %H:%M:%S")
load_dotenv()

db_url = os.getenv('account_uri')
db_key = os.getenv('account_key')
client = CosmosClient(db_url, credential=db_key, consistency_level='Session')
#fix azure.core.exceptions.ServiceResponseError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
database_name = 'democracy_bot'
database = client.get_database_client(database_name)
container_name = 'war_status'
container = database.get_container_client(container_name)

data = container.query_items(
    query='SELECT MAX(c.id) FROM c ', 
    enable_cross_partition_query=True)

data['id'] = stats['id'] + 1
data['/date'] = dt_formatted

session = requests.Session()
session.headers.update({'X-Super-Client': 'Democracy Bot','X-Super-Contact': 'gannonshanley@gmail.com'})
response = session.get("https://api.helldivers2.dev/api/v1/war")

war_stats = response.json()
war_stats = war_stats['statistics']
war_stats = {key: value for key,value in war_stats.items() if key not in ['revives','timePlayed','accuracy',]}
#new_stats = json.dumps(new_stats, default=lambda o: o.__dict__, sort_keys=True)
data.update(war_stats)

file = open('war_status.txt', 'w')
file.write(data)
file.close()

'''with open('war_status.txt', 'w') as file:
    json_string = json.dumps(stats_final, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    file.write(json_string)'''
