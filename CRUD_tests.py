import requests

createUserUrl = "https://petstore.swagger.io/v2/user"
getUserUrl = "https://petstore.swagger.io/v2/user/pyTestUser"
updatedUserUrl = "https://petstore.swagger.io/v2/user/pyTestUser1"



payload = ({ 
  "id": 0,
  "username": "pyTestUser1",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
})

myobj = {'id': 1, 'username': 'pyTestUser', 'firstName': 'firstName', 'lastName': 'lastName', 'email': 'email', 'password': 'password', 'phone': 'phone', 'userStatus': 0}
myobj2 = {'id': 2, 'username': 'pyTestUser1', 'firstName': 'firstName', 'lastName': 'lastName', 'email': 'email', 'password': 'password', 'phone': 'phone', 'userStatus': 0}


headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

headers1 = {}
payload1 = {}

createUser = requests.request("POST", createUserUrl, headers = headers, json = myobj)
response = requests.request("GET", getUserUrl, headers=headers, data={})
updatedUser = requests.request("PUT", getUserUrl, headers=headers, json=myobj2)
updatedUserR = requests.request("GET", updatedUserUrl, headers=headers, data={})
deletUser =  requests.request("DELETE", updatedUserUrl, headers=headers, data={})
updatedUserR2 = requests.request("GET", updatedUserUrl, headers=headers, data={})


print(createUser.text)
print(response.text)
print(updatedUser.text)
print(updatedUserR.text)
print(deletUser.text)
print(updatedUserR2.text)

