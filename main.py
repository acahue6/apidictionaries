# rest apis
#application programming interface

import requests  #request something from the internet 

response = requests.get("https://randomuser.me/api/")

#print(response.json())

gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)

names = response.json()['results'][0]['name']['first']
print(names)
names2 = response.json()['results'][0]['name']['last']
print(names2)

email = response.json()['results'][0]['email']
print(email)

phnumber = response.json()['results'][0]['phone']
print(phnumber)

city = response.json()['results'][0]['location']['city']
print(city)

postalcode = response.json()['results'][0]['location']['postcode']
print(postalcode)

streetaddress = response.json()['results'][0]['street']
print(streetaddress)

date = response.json()['results'][0]['dob']['date']
print(date)

age = response.json()['results'][0]['dob']['age']
print(age)

userid = response.json()['results'][0]['id']
print(userid)

