#coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'library.views.main', name='home'),      #主页
    url(r'^delete',  'library.views.delete'),           #删除
    url(r'^author',  'library.views.author'),           #更新作者
    url(r'^updata',  'library.views.updata'),           #更新
    url(r'^admin/', include(admin.site.urls)),
]