from django.shortcuts import render
from django.http import  HttpRequest
from django.http import HttpResponse
from django.core.paginator import Paginator
from item.models import Item
# Create your views here.

def index(request):
    limit=5
    item_list = Item.objects()
    paginator=Paginator(item_list,limit)
    page=request.GET.get('page',1)
    print page
    loaded=paginator.page(page)
    context ={
        'items':loaded
    }
    return render(request,'index.html',context)

def home(request):
    limit=5
    item_list = Item.objects()
    paginator=Paginator(item_list,limit)
    page=request.GET.get('page',1)
    print page
    loaded=paginator.page(page)
    context ={
        'items':loaded
    }
    return render(request,'home.html',context)

def chart(request):
    limit=5
    item_list = Item.objects()
    paginator=Paginator(item_list,limit)
    page=request.GET.get('page',1)
    print page
    loaded=paginator.page(page)
    context ={
        'items':loaded
    }
    return render(request,'chart.html',context)
