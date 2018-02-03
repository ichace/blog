# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Category,Tag,Blog,comment,message,link
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
class TagAdmin(admin.ModelAdmin):
    list_display1 = ('name',)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','author','put_date',)
    fields = ('title','author','contnet','cont_img','topped','category','tag','status',)
class CommentAdmin(admin.ModelAdmin):
    list_diaplay3=('user','comm_mail','comm_cont','status',)
    field=('blog','user','comm_mail','comm_cont','status',)
class MessageAdmin(admin.ModelAdmin):
    list_display4=('mess_nc','mess_mail','mess_cont','status')
class LinkAdmin(admin.ModelAdmin):
    list_display5=('name','link_url','link_des')
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(comment,CommentAdmin)
admin.site.register(message,MessageAdmin)
admin.site.register(link,LinkAdmin)
# Register your models here.
