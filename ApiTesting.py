import requests
import json
import jsonpath

def testGetResquest():
    url = 'https://reqres.in/api/users?page=2'
    # Get response
    response = requests.get(url)

    # Parse JSON 
    json_response = json.loads(response.text)

    # Fetch json value
    total = jsonpath.jsonpath(json_response, 'total')
    print(total[0])
    print(response.status_code)
    assert response.status_code == 200    

testGetResquest()
# print(total)
# print(response)