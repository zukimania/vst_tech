from django.urls import path,include
# from .views import *
from . import views


app_name="sitepages"

urlpatterns = [
    path('', views.Home, name= "home"),
    path('about/', views.About, name= "about"),
    path('service/', views.Service, name= "service"),
    path('contact/', views.Contact, name= "contact"),
    path('latest/', views.Latest, name= "latest"),
    path('post-detail/<int:pk>', views.PostDetail, name="post_detail"),
    path('vision/', views.Vision, name= "vision"),
]