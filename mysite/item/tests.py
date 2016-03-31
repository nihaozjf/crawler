from django.test import TestCase
from item.models import Item
# Create your tests here.

for item in Item.objects()[2]:
    print(item)
