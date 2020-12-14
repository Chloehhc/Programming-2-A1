# requests_test.py
# read and get information from http

import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# raise an error if there is one (stop program if there's an error)
response.raise_for_status()

# create a variable to store the file
f = open("Romeo_and_Juliet.txt", "wb")

# grab info from http and save it in the variable
for chunk in response.iter_content(1000000):
    f.write(chunk)

# write the file to disk
f.close()

# Other Code --------------------------------------------------------------------------------

# print(type(response))

# print(response.status_code) # if prints 200 means found something, if 404 means didn't

# text = response.text
# print(text[0:1000])