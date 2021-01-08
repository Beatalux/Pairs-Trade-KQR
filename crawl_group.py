#개선할 사항
# 모듈화
# stdin redirection
# selenium -> beautifulsoup

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

group_url="https://finance.naver.com/sise/sise_group.nhn?type=group"
idx=4


xpath = f'//*[@id="contentarea_left"]/table/tbody/tr[{idx}]/td[1]/a'

chrome_driver_path = 'C:/Users/kmucs/Downloads/chromedriver_win32/chromedriver.exe' #'chromedriver'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get(group_url)
contents = driver.find_element_by_css_selector('#contentarea_left > table > tbody')

group_url_list = [e.get_attribute('href') for e in contents.find_elements_by_tag_name('a')]
print(group_url_list)

file = open('group_url_list.txt','w')
file.write('\n'.join(group_url_list))
file.close()


        #req = requests.get(group_url+str(idx))
        #html = req.text
        #soup = BeautifulSoup(html, 'html.parser')
        #idx+=1
        #print(str(i)+'\n'+req.text)
        #print(str(idx)+'n'+element+'n')
except:
    print('페이지 끝!')
"""
