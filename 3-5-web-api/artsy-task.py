import requests
import json

client_id = 'aa1cff0333bf0e03466d'
client_secret = '47b02cbb9a804e216ed4dce64b1c6e34'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)  # разбираем ответ сервера
token = j["token"]  # достаем токен
headers = {"X-Xapp-Token" : token}  # создаем заголовок, содержащий наш токен

artist_list = []

with open(r"./dataset_24476_4.txt", encoding='utf-8') as in_f:
    for artist_id in in_f:
        r = requests.get(f"https://api.artsy.net/api/artists/{artist_id.strip()}", headers=headers)  # инициируем запрос с заголовком
        r.encoding = 'utf-8'
        j = json.loads(r.text)  # разбираем ответ сервера
        artist_list.append((j['sortable_name'], j['birthday']))

sorted_list = sorted(artist_list, key=lambda x: (x[1], x[0]))

with open(r"./dataset_24476_4_res.txt", "w", encoding='utf-8') as out_f:
    #for t in sorted_list:
    out_data = '\n'.join(str(e[0]) + "\t-\t" + str(e[1]) for e in sorted_list)
    out_f.write(out_data)

print(sorted_list)