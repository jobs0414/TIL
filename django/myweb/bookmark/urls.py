from django.urls import path 
from django.conf.urls import url
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'

urlpatterns = [
    path('',BookmarkLV.as_view(),name='index'),
    path('',BookmarkDV.as_view(), name='detail'),
]
