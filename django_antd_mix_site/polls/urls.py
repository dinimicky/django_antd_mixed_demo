# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 22:36
# @Author  : kaiji@xiaohongshu.com
# @File    : urls.py
# @Software: IntelliJ IDEA
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]