import requests
import json
from datetime import datetime
import os

#from dotenv import load_dotenv

#https://helldivers-2.github.io/api/docs/openapi/swagger-ui.html

now = datetime.now()
dt_string = now.strftime("%m%d%Y%H%M%S")
dt_formatted = now.strftime("%m-%d-%Y- %H:%M:%S")


session = requests.Session()
session.headers.update({'X-Super-Client': 'Democracy Bot','X-Super-Contact': 'gannonshanley@gmail.com'})
response = session.get("https://api.helldivers2.dev//api/v1/dispatches")

data = response.json()
'''stats = data['statistics']
stats['updatetime'] = dt_formatted
stats_final = {key: value for key,value in stats.items() if key not in ['revives','timePlayed','accuracy',]}

#war_status = requests.get("https://api.helldivers2.dev")
#war_status = requests.get("https://helldiverstrainingmanual.com/api/v1/war/status")'''

'''with open('dispatches.txt', 'w') as file:
    json_string = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    file.write(json_string)'''
