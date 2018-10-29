from django.urls import path
from cms import views


app_name = 'cms'

urlpatterns = [
    path('book/', views.book_list, name='book_list'),
    path('book/add/', views.book_edit, name='book_add'),
    path('book/modify/<int:book_id>/', views.book_edit, name='book_modify'),
    path('book/delete/<int:book_id>/', views.book_remove, name='book_remove'),
]
