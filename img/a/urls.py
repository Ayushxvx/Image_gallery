from django.urls import path 
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("elaborate/<str:id>",elaborate,name="elaborate")
]
