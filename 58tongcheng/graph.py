# -*- coding:utf-8 -*-
import pymongo
from string import punctuation
from datetime import  timedelta,date
import charts

client =pymongo.MongoClient('localhost',27017)
db =client['crawler']
item_info = db['ganji']

#for i in item_info.find().limit(300):
#   print i['area']
def update_area(item_info):
    for i in item_info.find():
        #print i
        if i['area']:
            area = [k for k in i['area'] if k not in punctuation]
        else:
            area=['unknown']

        #print i['area']
        item_info.update({'_id':i['_id']},{'$set':{'area':area}})
def print_item_detail(item_info):
    for i in item_info.find():
        print i['area']

#print_item_detail(item_info)
#charts.plot()
def get_all_dates(start_date,end_date):
    the_date =date(int(start_date.split('.')[0]),int(start_date.split('.')[1]),int(start_date.split('.')[2]))
    the_end =date(int(end_date.split('.')[0]),int(end_date.split('.')[1]),int(end_date.split('.')[2]))
    #print the_end
    days = timedelta(days=1)
    while the_date<=the_end:
        yield the_date.strftime('%Y.%m.%d')
        the_date = the_date+days


def get_all_post(start_date,end_date,cate_list):
    count=0
    for cate in cate_list:

        cate_post_times=[]
        for date in get_all_dates(start_date,end_date):
            items = item_info.find({'pub_date':date,'cates':cate})

            cate_post_times.append(len(list(items)))
        #count +=1
        #name=str(count)
        adata={
            'name':cate,
            'data':cate_post_times,
            'type':'line'
        }
        yield adata
def get_one_day_items(day):
    pipeline =[
        {'$match':{'pub_date':day}},
        {'$group':{'_id':{'$slice':['$area',1]},'counts':{'$sum':1}}},


    ]
    items =item_info.aggregate(pipeline)
    return items
def draw_one_day_items(day):
    data=[]
    for item in  get_one_day_items(day):

        if item['_id']!=None:
            if len(item['_id'])==0:
                item['_id']=['unkown']
            data.append([item['_id'][0],item['counts']])
    #print data
    series={
        'type':'pie',
        'name':'pie chart',
        'data':data

    }
    return series
if __name__=='__main__':
    #print 'start'
    #items =get_all_post('2016.01.12','2016.01.12',['\u5317\u4eac\u4e8c\u624b\u5bb6\u7535'])
    #series=[i for i in get_all_post('2016.01.12','2016.01.19',['北京二手家电','北京二手手机','北京二手笔记本'])]

    #charts.plot(series,show='window')
    #print 'end'
    series=draw_one_day_items('2015.12.29')
    print series
    charts.plot(series,show='window')


