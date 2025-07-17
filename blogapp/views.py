from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from blogapp.models import Blog

def my_blog(response):
    var=Blog.objects.all()
    return render(request,"base.html",{'var':var})

