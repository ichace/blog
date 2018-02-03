# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
    content=RichTextUploadingField()
class Category(models.Model):
    name=models.CharField('标题',max_length=50)
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField('标签',max_length=30,)
    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name


class Blog(models.Model): 
    title=models.CharField('标题',max_length=32)
    author=models.CharField('作者',max_length=16,default='admin')
    contnet=RichTextField('内容',blank=True)
    cont_img=models .ImageField('内容主图',upload_to='images/',default='images/defaut.jpg')
    views=models.PositiveIntegerField('浏览量',default=0)
    likes=models.PositiveIntegerField('点赞',default=0)
    put_date=models.DateField('发表时间',auto_now_add=True)
    topped=models.BooleanField('置顶',default=False)
    category=models.ForeignKey(Category,verbose_name='分类')
    tag=models.ManyToManyField(Tag,verbose_name='标签',default='日记',null=True,blank=True)
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    status=models.CharField('状态',max_length=1,choices=STATUS_CHOICES)
    def increase_views(self):
        self.views=self.views+1
        self.save(update_fields=['views'])
    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.title
        # Create your models here.

#评论
class comment(models.Model):
    blog=models.ForeignKey(Blog,verbose_name="博客")
    user=models.CharField('用户',max_length=30)
    comm_ip=models.GenericIPAddressField('ip')
    comm_mail=models.EmailField('邮箱')
    comm_cont=models.CharField('内容',max_length=54)
    comm_date=models.DateField('发表时间',auto_now_add=True)
    STATUS_CHOICES={
        ('t','True'),
        ('f','False')
    }
    status=models.CharField('状态',max_length=1,choices=STATUS_CHOICES)
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name


#留言
class message(models.Model):
    mess_ip=models.GenericIPAddressField('ip')
    mess_nc=models.CharField('昵称',max_length=50)
    mess_mail=models.EmailField('邮箱')
    mess_cont=models.CharField('留言内容',max_length=54)
    mess_date=models.DateField('发表时间',auto_now_add=True)
    STATUS_CHOICES={
        ('t','true'),
        ('f','False')
    }
    status=models.CharField('状态',max_length=1,choices=STATUS_CHOICES)
    class Meta:
        verbose_name='留言'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.mess_cont

#友情链接
class link(models.Model):
    name=models.CharField('链接名称',max_length=30)
    link_url=models.URLField('链接地址')
    link_des=models.CharField('链接描述',max_length=54,null=True,blank=True)
    STATUS_CHOICES={
        ('t','true'),
        ('f','False')
    }
    status=models.CharField('状态',max_length=1,choices=STATUS_CHOICES)
    class Meta:
        verbose_name='友情链接'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name