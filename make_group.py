# 그룹사에 속한 종목별로 그룹핑하는 코드
# 모듈화
# stdin redirection?

import requests
from bs4 import BeautifulSoup
import os

f = open('group_url_list.txt','r')

group_urls = f.readlines()
group_stocks_list = [[] for _ in group_urls]

for i,url in enumerate(group_urls):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')

    # *붙은 종목 처리, l.text.strip('*') 안돼서 형변환함
    # 공백제거
    group_stocks_list[i] = [str(l.text).strip('*').strip(' ') for l in soup.find_all('div',attrs={"class":"name_area"})]

print(group_stocks_list)
if os.path.exists('./group_stock_file.txt'):
    print('file 있음. 종료')
else:
    group_stocks_file = open('group_stock_file.txt','w')
    print(([','.join(i) for i in group_stocks_list]))
    group_stocks_file.write('\n'.join([','.join(i) for i in group_stocks_list]))
    group_stocks_file.close()
