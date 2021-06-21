import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Example of making a POST request

link = 'http://localhost:5000/example-post'

# data to make POST request with
data = {
    "name" : "your name",
    "age" : 0 # add your age here
}
response = requests.post(link, json=data)

responseDict = response.json()
pp.pprint(responseDict)


