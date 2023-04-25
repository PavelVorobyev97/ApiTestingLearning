import requests
import json

url = 'https://reqres.in/api/users?page=2'
# Get response
response = requests.get(url)

# Parse JSON 
json_response = json.loads(response.text)

print(json_response)