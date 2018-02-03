# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import Category,Blog,Tag,link,message
from django.http import HttpResponse

from django import forms

class lyform(forms.Form):
    name=forms.CharField(max_length=30,label='昵称')
    cont=forms.CharField(max_length=200,label='内容',widget=forms.Textarea)
def index(request):
    mess=message.objects.all().order_by('-mess_date')
    blog=Blog.objects.filter(status='p').order_by('-views')
    cat=Category.objects.all()
    tag=Tag.objects.all()
    link_=link.objects.all()
    a=[]
    for i in blog:  #将标签合并到blog
        a.append(i.tag.all())
    blog=zip(blog,a)
    url= request.build_absolute_uri()
    url=url[:-1]
    return render(request,'index.html',{'blog':blog,'cat':cat,'tag':tag,'link_':link_,'a':a,'url':url,'mess':mess})
def bk(request,id):
    blog=Blog.objects.get(id=id)
    blog.increase_views()
    mess=message.objects.all()
    tag=Tag.objects.all()
    link_=link.objects.all()
    if request.method=="GET":
        return render(request,'blog-info.html',{'blog':blog,'mess':mess,'mess':mess,'tag':tag,'link':link_})
def fl(request,id):
    ccc=Category.objects.get(id=id)
    blog=Blog.objects.filter(category=ccc)
    tag=Tag.objects.all()
    link_=link.objects.all()
    cat =Category.objects.all()
    mess=message.objects.all().order_by('-mess_date')
    a=[]
    for i in blog:
        a.append(i.tag.all())
    blog=zip(blog,a)
    return render(request,'index.html',{'blog':blog,'cat':cat,'tag':tag,'link_':link_,'a':a,'mess':mess})
def bq(request,id):
    ccc=Tag.objects.get(id=id)
    blog=Blog.objects.filter(tag=ccc)
    tag=Tag.objects.all()
    link_=link.objects.all()
    cat =Category.objects.all()
    a=[]
    for i in blog:
        a.append(i.tag.all())
    blog=zip(blog,a)
    return render(request,'index.html',{'blog':blog,'cat':cat,'tag':tag,'link_':link_,'a':a})

def ly(request):
    if request.method=="POST":
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        name= request.POST.get('name')
        nr=request.POST.get('cont')
        email=request.POST.get('email')
        print name,nr,email
        aa=message(mess_ip=ip,mess_cont=nr,mess_mail=email,mess_nc=name,)
        aa.save()
        return HttpResponse('成功')
    else:
        cat=Category.objects.all()
        tag=Tag.objects.all()
        link_=link.objects.all()
        url= request.build_absolute_uri()
        url=url[:-1]
        mess=message.objects.all().order_by('-mess_date')
        return render(request,'play/ly.html',{'cat':cat,'tag':tag,'link_':link_,'url':url,'lyform':lyform,'mess':mess,})

# Create your views here.
