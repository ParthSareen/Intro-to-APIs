import requests

print("hi")

response = requests.get("https://api.open-notify.org/astros.json")
print(response.json)
