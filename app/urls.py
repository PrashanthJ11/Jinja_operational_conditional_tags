from django.urls import path

from app.views import *

app_name='anything'

urlpatterns=[
    path('rishi/',rishi,name='rishi'),
    path('loki/',loki,name='loki'),
    path('shaju/',shaju,name='shaju'),
    path('praveen/',Praveen,name='praveen'),
]