import requests

# city = input('City? - ')
cs_nums = ''
lines = ''

with open('dataset_24476_3.txt', 'r') as f:
    lines = [line.strip() for line in f]
    cs_nums = ','.join(lines)

api_url = f'http://numbersapi.com/{cs_nums}/math?json=true'


res = requests.get(api_url)
print(res.status_code)
print(res.headers['Content-Type'])
print(res.json())
data = res.json()
text = data['text']
print(text)