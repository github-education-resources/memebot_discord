import requests
import json
from datetime import datetime
import os
import ast
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

#https://helldivers-2.github.io/api/docs/openapi/swagger-ui.html

now = datetime.now()
dt_string = now.strftime("%m%d%Y%H%M%S")
dt_formatted = now.strftime("%m-%d-%Y- %H:%M:%S")

load_dotenv()
db_uri = os.getenv('account_uri')
db_key = os.getenv('account_key')
headers = ast.literal_eval(os.getenv('header1'))

client = CosmosClient(url=db_uri, credential=db_key)
database_name = 'democracy_bot'
database = client.get_database_client(database_name)
container_name = 'war_status'
container = database.get_container_client(container_name)

data = {}
#gets only the highest ID for db key since the data doesnt have one itself
for item in container.query_items(
        query='SELECT c.id as id FROM war_status c ORDER BY c.id DESC OFFSET 0 LIMIT 1',
        enable_cross_partition_query=True):
    data.update(item)

#formats data to table schema
data['id'] = str(int(data['id']) + 1)
data['/date'] = dt_formatted

session = requests.Session()
session.headers.update(headers)
response = session.get("https://api.helldivers2.dev/api/v1/war")

war_stats = response.json()
war_stats = war_stats['statistics']
war_stats = {key: value for key,value in war_stats.items() if key not in ['revives','timePlayed','accuracy',]}
#new_stats = json.dumps(new_stats, default=lambda o: o.__dict__, sort_keys=True)
data.update(war_stats)

container.upsert_item(data)

#test dumping to file
'''file = open('war_status.txt', 'w')
file.write(data)
file.close()'''

'''with open('war_status.txt', 'w') as file:
    json_string = json.dumps(stats_final, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    file.write(json_string)'''
