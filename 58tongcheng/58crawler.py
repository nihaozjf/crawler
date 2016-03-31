#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import  time

baseURL='http://bj.58.com/pbdn/0/'
testUrl='http://bj.58.com/pingbandiannao/25317032512076x.shtml'
countUrl='http://jst1.58.com/counter?infoid='
count =0
def getLinks(url):
    global  count
    html = requests.get(url).content
    soup = BeautifulSoup(html,'lxml')
    #print soup
    urls=[]
    links = soup.select(' td.t > a')
    for link in links:
        url=link['href']
        if 'pingbandiannao' in url:
            #print url.split('?')[0]
            urls.append(url.split('?')[0])
            count = count+1
    return urls
def getDetail(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('div.col_sub.mainTitle > h1')[0]
    #print title.getText()
    posttime=soup.select('ul.mtit_con_left.fl > li.time')[0]
    #print posttime.getText()
    price =soup.select('div.su_con > span')[0]
    #print price.getText()
    '''
    http://bj.58.com/pingbandiannao/25317032512076x.shtml?psid=119026246191075957146493037&entinfo=25317032512076_0
    http://user.58.com/userdata/?callback=jsonp8617&userid=37721819351823&type=26&cityid=1&dispcateid=38484
    http://user.58.com/userdata/?callback=jsonp1936&userid=37968787697425&type=26&cityid=1&dispcateid=38484
    '''
    poster=soup.select('#divContacter a.tx')
   # print poster
    viewsUrl=countUrl+url.split('/')[-1][:-7]
    views =getCounts(viewsUrl)
    #print views
    area=soup.select('.c_25d')[0]
    print area
    print list( area.stripped_strings)

def getCounts(url):
    res=requests.get(url).content
    return res.split('=')[-1]
#print getLinks(baseURL)
#print count
getDetail(testUrl)
#getCounts(countUrl)