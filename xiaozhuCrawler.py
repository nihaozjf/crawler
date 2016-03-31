#!encoding:utf-8
import requests
from bs4 import BeautifulSoup
import time
count=0
'''url='http://bj.xiaozhu.com/fangzi/1508951935.html'
html = requests.get(url).content
soup = BeautifulSoup(html,'lxml')

title=soup.select('div.pho_info > h4 > em')[0].getText()
#print title
addr= soup.select('div.pho_info > p')[0].get('title')
#print addr
price =soup.select('#pricePart > div.day_l > span')[0].getText()
#print price.getText()
img = soup.select('div.member_pic > a > img')[0].get('src')
#print img
host_name=soup.select('div.w_240 > h6 > a')[0].get('title')
#print host_name
host_gender=soup.select('div.member_pic > div')[0].get('class')[0]
#print host_gender

def get_gender(icon):
    if icon=='member_ico1':
        return 'female'
    else:
        return 'male'

data={'title':title,
       'addr':addr,
       'price':price,
       'img':img,
       'host_name':host_name,
       'host_gender':get_gender(host_gender)}
print data
#page_list > ul > li:nth-child(1) > a
'''
def get_page(url):
    global  count
    html = requests.get(url).content
    soup =BeautifulSoup(html,'lxml')
    links=soup.select('#page_list > ul > li > a:nth-of-type(1)')
    for link in links:

        print get_detail(link['href'])
        count =count+1
        time.sleep(1)

def get_detail(link):

    html = requests.get(link).content
    soup = BeautifulSoup(html,'lxml')
    title=soup.select('div.pho_info > h4 > em')[0].getText()
    #print title
    addr= soup.select('div.pho_info > p')[0].get('title')
    #print addr
    price =soup.select('#pricePart > div.day_l > span')[0].getText()
    #print price.getText()
    img = soup.select('div.member_pic > a > img')[0].get('src')
    #print img
    host_name=soup.select('div.w_240 > h6 > a')[0].get('title')
    data={'title':title,
       'addr':addr,
       'price':price,
       'img':img,
       'host_name':host_name
       }
    return data

urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,2)]
#print urls
for url in urls:
    #print url
    get_page(url)
    print count