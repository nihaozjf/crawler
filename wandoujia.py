#-*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
db=client.crawler
app=db.wandoujia

urls=['http://www.wandoujia.com/category/392_{}'.format(str(i)) for i in range(1,43)]
count=0

def getLinks(url):
    global  count
    html = requests.get(url).content
    soup =BeautifulSoup(html,'lxml')
    #print soup
    links = soup.select('div.app-desc > h2 > a')
    for link in links:
        data=getDetail( link['href'])
        #print data
        app.insert(data)
        count = count+1
        time.sleep(1)

def getDetail(link):
    #print link
    app_html  =requests.get(link).content
    app_soup = BeautifulSoup(app_html,'lxml')
    app_title=app_soup.select('div.app-info > p.app-name > span')[0]
    #print app_title.getText()
    app_install=app_soup.select('div.num-list > span:nth-of-type(1) > i')[0]
    #print app_install.getText()
    app_size=app_soup.select('div.col-right > div > dl > dd:nth-of-type(1)')[0]
    #print app_size.getText().strip()
    app_like=app_soup.select('span.item.love > i')[0]
    #print 'app like:\t'+app_like.getText()
    app_comment=app_soup.select('a.item.last.comment-open > i')[0]
    app_category=app_soup.select('div.col-right > div > dl > dd.tag-box')[0]
    #print app_category.getText().strip()
    #print app_title.getText()+'\t'+app_like.getText()+'\t'+app_comment.getText()
    app_description=app_soup.select('div.desc-info > div')[0]
    #print app_description.getText().strip()
    '''app_info =app_title.getText()+'$'+\
              app_install.getText()+'$'\
              +app_size.getText().strip()+'$'\
              +app_like.getText()+'$'\
              +app_comment.getText()+'$'\
              +app_category.getText().strip()+'$'\
              +app_description.getText().strip()
    return app_info'''
    '''data={
        'title':app_title.getText().encode('utf-8'),
        'install':app_install.getText().encode('utf-8'),
        'size':app_size.getText().strip().encode('utf-8'),
        'likes':app_like.getText().encode('utf-8'),
        'comments':app_comment.getText().encode('utf-8'),
        'category':app_category.getText().strip().encode('utf-8'),
        'description':app_description.getText().strip().encode('utf-8')
    }'''
    data={
        'title':app_title.getText(),
        'install':app_install.getText(),
        'size':app_size.getText().strip(),
        'likes':app_like.getText(),
        'comments':app_comment.getText(),
        'category':app_category.getText().strip(),
        'description':app_description.getText().strip()
    }
    return data



def crawl():
    for url in urls:
        #print url
        getLinks(url)
        time.sleep(1)
    print count
crawl()