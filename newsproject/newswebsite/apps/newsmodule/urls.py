from django.urls import path, include
from apps.newsmodule import views

urlpatterns = [
path('', views.index,name='index')   
]


