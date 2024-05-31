import requests
import json
from datetime import datetime
import os
import ast
from dotenv import load_dotenv
from azure.cosmos import CosmosClient
import re

#load keys
load_dotenv()
db_uri = os.getenv('account_uri')
db_key = os.getenv('account_key')
headers = ast.literal_eval(os.getenv('header1'))

#create db connection
client = CosmosClient(url=db_uri, credential=db_key)
database_name = 'democracy_bot'
database = client.get_database_client(database_name)
container_name = 'dispatch'
container = database.get_container_client(container_name)

#connect to api
session = requests.Session()
session.headers.update(headers)
response = session.get("https://api.helldivers2.dev//api/v1/dispatches")
data = response.json()

#format for the database
for item in data:
    item['id'] = str(item['id'])
    item['/id'] = item['id']
    item['message'] = re.sub('<i=\d>|</i>', '**', item['message'])

#queries for last uploaded id
for item in container.query_items(
        query='SELECT c.id as id FROM dispatch c ORDER BY c.id DESC OFFSET 0 LIMIT 1',
        enable_cross_partition_query=True):
    lastid = item

#inserts new items into db
for item in data:
    if int(item['id']) > int(lastid['id']):
        container.upsert_item(item)
