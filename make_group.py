# 그룹사에 속한 종목별로 그룹핑하는 코드
# 모듈화
# stdin redirection?

#import re
import requests
from bs4 import BeautifulSoup
import os

f = open('group_url_list.txt','r')

group_urls = f.readlines()
group_stocks_list = [[] for _ in group_urls]

for i,url in enumerate(group_urls):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')

    #print(soup.find("a")) 관련없는 a tag 있어서 안됨


    #두개는 같은 결과
    #print(soup.find_all(attrs={"class":"name_area"}))
    #print(soup.find_all('div', attrs={"class": "name_area"}))

    # *붙은 종목 처리, l.text.strip('*') 안돼서 형변환함
    group_stocks_list[i] = [str(l.text).strip('*').strip(' ') for l in soup.find_all('div',attrs={"class":"name_area"})]

print(group_stocks_list)
if os.path.exists('./group_stock_file.txt'):
    print('file 있음. 종료')
else:
    group_stocks_file = open('group_stock_file.txt','w')
    print(([','.join(i) for i in group_stocks_list]))
    group_stocks_file.write('\n'.join([','.join(i) for i in group_stocks_list]))
    group_stocks_file.close()
    #print('\n')
    #pattern = re.split('< | >',str(soup.find(attrs={"class":"name_area"})))
    #print(pattern)
    #print(str(soup.find(attrs={"class":"name_area"})).split('<[a-z]+>'))

    #print(soup.find(attrs={"href": f"/item/main.nhn?code={[0-9]+}"}))

    #print(soup.select('contentarea > div > table > tbody > tr'))
#contentarea > div:nth-child(5) > table > tbody > tr:nth-child(1) > td.name > div > a
#contentarea > div:nth-child(5) > table > tbody > tr:nth-child(2) > td.name > div > a

#group_urls[i].append()