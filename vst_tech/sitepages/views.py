from django.shortcuts import render
from .models import Post



def Index(request):
    featured_post = Post.objects.all().filter(category=0)[:1]
    django_post = Post.objects.all().filter(fram=0)[:2]
    flask_post = Post.objects.all().filter(fram=1)[:2]
    data={"featured_post": featured_post, 'django_post':django_post, 'flask_post': flask_post}
    return render (request,"sitepages/index.html", data)

def About(request):
    return render (request,"sitepages/about.html")

def Service(request):
    return render (request,"sitepages/service.html")

def Contact(request):
    return render (request,"sitepages/contact.html")

def Latest(request):
    featured_post = Post.objects.all().filter(category=0)[:1]
    django_post = Post.objects.all().filter(fram=0)[:2]
    flask_post = Post.objects.all().filter(fram=1)[:2]
    data={"featured_post": featured_post, 'django_post':django_post, 'flask_post': flask_post}
    return render (request,"sitepages/latest.html", data)

def PostDetail(request,pk):
    post_detail = Post.objects.filter(pk=pk)
    data={"post_detail": post_detail}
    return render (request,"sitepages/post_detail.html", data)

def Vision(request):
    data={"ptitle": "Meals order & bookings - Home Page"}
    return render (request,"sitepages/vision.html", data)

