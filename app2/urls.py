from django.urls import path 
from app2.views import *

app_name='app2'


urlpatterns=[

    path('sister2/',sister2,name='sister2'),
]