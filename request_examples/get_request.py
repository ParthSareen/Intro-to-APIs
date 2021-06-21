import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Example for making a GET requests

link = 'http://localhost:5000/example-get-static'
response = requests.get(link)

responseDict = response.json()
pp.pprint(responseDict)

# access the dict
print(responseDict['num-example'])

# your name goes here
name = "name"
link2 = 'http://localhost:5000/example-get-dynamic?name={name}'.format(name=name)

response = requests.get(link2)

responseDict = response.json()
pp.pprint(responseDict)



