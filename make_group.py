# 그룹사에 속한 종목별로 그룹핑하는 코드
# 모듈화
# stdin redirection?

#import re
import requests
from bs4 import BeautifulSoup

f = open('group_url_list.txt','r')

group_urls = f.readlines()
group_urls_list = [[] for _ in group_urls]

for i in group_urls:
    html = requests.get(i)
    soup = BeautifulSoup(html.text,'html.parser')

    #print(soup.find("a")) 관련없는 a tag 있어서 안됨


    #두개는 같은 결과
    #print(soup.find_all(attrs={"class":"name_area"}))
    #print(soup.find_all('div', attrs={"class": "name_area"}))

    # *붙은 종목 처리, l.text.strip('*') 안돼서 형변환함
    a = [str(l.text).strip('*') for l in soup.find_all('div',attrs={"class":"name_area"})]
    print(a)

    #print('\n')
    #pattern = re.split('< | >',str(soup.find(attrs={"class":"name_area"})))
    #print(pattern)
    #print(str(soup.find(attrs={"class":"name_area"})).split('<[a-z]+>'))

    #print(soup.find(attrs={"href": f"/item/main.nhn?code={[0-9]+}"}))

    #print(soup.select('contentarea > div > table > tbody > tr'))
#contentarea > div:nth-child(5) > table > tbody > tr:nth-child(1) > td.name > div > a
#contentarea > div:nth-child(5) > table > tbody > tr:nth-child(2) > td.name > div > a

#group_urls[i].append()