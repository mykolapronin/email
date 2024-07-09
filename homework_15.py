import requests
import json

# first part
# with open('fable.pdf', mode='bw') as my_file:
#     response = requests.get('https://shron1.chtyvo.org.ua/Falkovych_Hryhorii/Smyk-tyndyk.pdf?PHPSESSID=jriev9ga4aorsnld0autpih5d3')
#     print(response.content)
#     my_file.write(response.content)

# second part

url = 'http://api.open-notify.org/astros.json'
response1 = requests.get(url=url)
data = response1.json()
with open('data.json', mode='w') as file:
    json.dump(data, file, indent=4)

