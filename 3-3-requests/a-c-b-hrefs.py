import requests
from bs4 import BeautifulSoup

answer = 'No'
link_to_a, link_to_b = input(), input()

res_a = requests.get(link_to_a)
soup_a = BeautifulSoup(res_a.text, features="lxml")

for link_in_a in soup_a.findAll('a'):

    link_to_c = link_in_a.get('href')
    res_c = requests.get(link_to_c)
    soup_c = BeautifulSoup(res_c.text, features="lxml")

    for link_in_c in soup_c.findAll('a'):
        if link_in_c.get('href') == link_to_b:
            answer = 'Yes'
            break
    else:
        continue
    break

print(answer)
