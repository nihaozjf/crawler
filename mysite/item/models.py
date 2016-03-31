from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.
class Item(Document):
    category=StringField()
    description =StringField()
    title = StringField()
    comments =StringField()
    likes=StringField()
    install=StringField()
    size=StringField()
    meta={
        'collection':'wandoujia'
    }

