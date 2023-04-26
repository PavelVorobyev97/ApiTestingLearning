import requests
import json
import jsonpath

def testGetRequest():
    url = 'https://reqres.in/api/users?page=2'
    # Get response
    response = requests.get(url)    
    # Parse JSON 
    json_response = json.loads(response.text)

    # Fetch total json value
    total = jsonpath.jsonpath(json_response, 'total')
    # print(total[0])
    print("Get /users?page=2 code:" + str(response.status_code))

    # Assert status code
    assert response.status_code == 200

def testDelete():
    url = 'https://reqres.in/api/users/2'
    # Get response
    response = requests.delete(url)
    
    print("Delete /users/2 code:" + str(response.status_code))
    
    # Assert status code
    assert response.status_code == 204

def testPostAddUser():
    url = 'https://reqres.in/api/users'
    file = open('testData/createUserData', 'rb')
    json_message = file.read()
    print(json_message)
    response = requests.post(url, json_message)

    print("Post api/users code:" + str(response.status_code))
    # print(response.content) 
    
    # Assert status code
    assert response.status_code == 201   

testGetRequest()
testDelete()
testPostAddUser()
