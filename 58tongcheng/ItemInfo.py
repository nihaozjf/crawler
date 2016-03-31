#-*-coding:utf-8 -*-
import  multiprocessing as mul
from multiprocessing import pool
import  requests
import  time
from bs4 import  BeautifulSoup
from time import clock
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['crawler']
item_url_db= db['item_url']
item_info = db['item_info']
item_urls=[item['item_url'] for item in item_url_db.find()]
count = 0
countUrl='http://jst1.58.com/counter?infoid='
#testUrl='http://bj.58.com/pingbandiannao/25317032512076x.shtml'
#testUrl='http://bj.58.com/pingbandiannao/25338567591723x.shtml'
testUrl='http://bj.58.com/pingbandiannao/25290756415788x.shtml'
def get_item_info(url):
    res=requests.get(url)
    html=res.text.encode('utf-8')
    soup =BeautifulSoup(html,'lxml')
    not_exist='404'in soup.find('script',type='text/javascript').get('src').split('/')
   # print not_exist
    data={}
    if not_exist:
        pass
    else:
        global  count
        title = soup.select('div.col_sub.mainTitle > h1')[0]
        #print title.getText()
        posttime=soup.select('ul.mtit_con_left.fl > li.time')[0]
        #print posttime.getText()
        price =soup.select('div.su_con > span')[0]
        #print price.getText()
        viewsUrl=countUrl+url.split('/')[-1][:-7]
        #print 'viewsUrl\t'+viewsUrl
        views =getCounts(viewsUrl)
        #print views
        area=list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d')else None
        #print area
        data={
            'item_url':url,
            'title':title.getText(),
            'posttime':posttime.getText(),
            'price':price.getText(),
            'views':views,
            'area':area
        }
        print data
        item_info.insert(data)

        count=count+1
    #return data



def getCounts(url):
    res=requests.get(url).content
    return res.split('=')[-1]

def get_item_by_url(urls):

    pool =mul.Pool()

    t1 =clock()
    pool.map(get_item_info,urls)
    t2=clock()
    print 'time\t'+str(t2-t1)
    print 'total count\t'+str(count)

#print get_item_info(testUrl)
test_item_urls=['http://bj.58.com/pingbandiannao/25338567591723x.shtml',
           'http://bj.58.com/pingbandiannao/25338567591724x.shtml',
           'http://bj.58.com/pingbandiannao/25338887050698x.shtml',
            'http://bj.58.com/bijibendiannao/25290413315625x.shtml']

if __name__=='__main__':
    get_item_by_url(item_urls)