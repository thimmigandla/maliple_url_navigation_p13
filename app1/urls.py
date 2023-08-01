from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('sister1/',sister1,name='sister1'),
]