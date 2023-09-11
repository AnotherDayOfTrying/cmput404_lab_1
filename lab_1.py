import requests

# VERSION OF REQUEST PACKAGE
print(requests.__version__)

# GOOGLE MAIN PAGE
response = requests.get('http://www.google.com')
print(response.content)

#PRINT SOURCE CODE
response = requests.get('https://raw.githubusercontent.com/AnotherDayOfTrying/cmput404_lab_1/main/lab_1.py')
print(response.content)
