import requests

print(requests.__version__)

r = requests.get('http://www.google.com')

print(r.content)


r = requests.get('GITHUB URL HERE')

#PRINT CODE

print(r.content)
