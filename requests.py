import requests, json

# geralmente se usa a lib requests com a lib beatifullsoap

r = requests.get('https://api.github.com/users/julianofischer')
j = json.loads(r.text)
print(j)