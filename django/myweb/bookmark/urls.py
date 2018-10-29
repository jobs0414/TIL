from django.urls import path 
from django.conf.urls import url
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [
    path('',BookmarkLV.as_view(),name='index'),
    path('<int:pk>/',BookmarkDV.as_view(), name='detail'),


    path('add/',BookmarkCreateView.as_view(), name='add'), 
    path('change/',BookmarkChangeLV.as_view(), name='change'), 
    path('update/<int:pk>',BookmarkUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>',BookmarkDeleteView.as_view(), name='delete'), 

]
