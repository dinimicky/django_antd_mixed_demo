# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 22:36
# @Author  : kaiji@xiaohongshu.com
# @File    : urls.py
# @Software: IntelliJ IDEA
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]