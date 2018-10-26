from django.urls import path 
from django.conf.urls import url 
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # /blog/ 
    path('',PostLV.as_view(),name='index'),
     
     #/blog/post
    path('post',PostLV.as_view(), name='post_list'),

    #/blog/post/python-programming 

    path('post/<str:slug>', PostDV.as_view(), name ='post_detail'), 

    #/blog/archieve 
    path('archive', PostAV.as_view(), name="post_archive"), 

    #/blog/2018 
    path('<int:year>',PostYAV.as_view(),name="post_year_archive"),

    #/blog/2018/nov 
    path('<int:year>/<str:month>',PostMAV.as_view(),name="post_month_archive"),

    #/blog/2018/nov/12 
    path('<int:year>/<str:month>/<int:day>',PostDAV.as_view(),name="post_day_archive"),

    #/blog/today 
    path('today',PostTAV.as_view(),name="post_today_archive"),

    path ('search/', SearchFormView.as_view(), name='search'),

]
