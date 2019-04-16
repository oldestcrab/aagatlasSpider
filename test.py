import requests

url = 'http://biokb.ncpsb.org/aagatlas/index.php/Home/Download/disease/term/acute%20gastric%20ulcer%20with%20hemorrhage%20AND%20obstruction%20(disorder)/id/do~doid:10808'
response = requests.get(url)
print(type(response))
print(response.text)
with open('./sg.csv', 'wb') as f:
    f.write(response.content)