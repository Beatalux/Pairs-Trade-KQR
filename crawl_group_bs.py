import requests
from bs4 import BeautifulSoup

group_url="https://finance.naver.com/sise/sise_group.nhn?type=group"
html = requests.get(group_url)
soup = BeautifulSoup(html.text,'html.parser')

group_object = soup.select('contentarea_left > table > tbody > tr > td > a')[0]
print(group_object)
#group_url = [group_object.]