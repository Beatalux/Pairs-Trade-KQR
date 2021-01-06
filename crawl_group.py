import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#group_url = "https://finance.naver.com/sise/sise_group.nhn?type=group"

group_url="https://finance.naver.com/sise/sise_group.nhn?type=group"
idx=4

#contentarea_left > table > tbody > tr:nth-child(4) > td:nth-child(1) > a

xpath = f'//*[@id="contentarea_left"]/table/tbody/tr[{idx}]/td[1]/a'
#//*[@id="contentarea_left"]/table/tbody/tr[79]/td[1]/a

chrome_driver_path = 'C:/Users/kmucs/Downloads/chromedriver_win32/chromedriver.exe' #'chromedriver'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get(group_url)
contents = driver.find_element_by_css_selector('#contentarea_left > table > tbody')
#driver.findelement
#print(contents.find_elements_by_tag_name('a'))
"""
group_url_list = []
for e in contents.find_elements_by_tag_name('a'):
    print(e.get_attribute('href'), e.text)
"""
group_url_list = [e.get_attribute('href') for e in contents.find_elements_by_tag_name('a')]
print(group_url_list)
"""
try:
    while idx<=79:
        if (idx-4)%5==0:
            pass
        selector = f'#contentarea_left > table > tbody > tr:nth-child({idx}) > td:nth-child(1) > a'

        #stock = driver.find_element_by_css_selector(selector)
        contents = driver.find_element_by_id('contentarea_left')
        #print(selector,stock.text,idx)
        idx+=1
        #element = driver.find_elements_by_xpath(xpath)
        #doc = driver.get(product_url)

        #req = requests.get(group_url+str(idx))
        #html = req.text
        #soup = BeautifulSoup(html, 'html.parser')
        #idx+=1
        #print(str(i)+'\n'+req.text)
        #print(str(idx)+'n'+element+'n')
except:
    print('페이지 끝!')
"""