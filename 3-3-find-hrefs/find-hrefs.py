import requests
import re
from bs4 import BeautifulSoup

link = "http://pastebin.com/raw/hfMThaGb"
pat = r"(([a-z0-9|-]+\.)*[a-z0-9|-]+\.[a-z]+)"
out_list = []
req_res = requests.get(link)
soup = BeautifulSoup(req_res.text, features="lxml")

for anchor in soup.findAll('a'):
    link = anchor.get('href')
    if link is None:
        continue
    if link.find("0123d.ifmo.ru") >= 0:
        asd = 5
    groups = re.search(pat, link)
    if groups is None:
        continue
    out_list.append(groups.group(1))

out_set = set(out_list)
out_list = list(out_set)
out_list.sort()
print(*out_list, sep='\n')




