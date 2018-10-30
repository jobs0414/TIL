from django.urls import path,include
from api import views 

app_name ="api"


urlpatterns = [
    #도서목록 http://127.0.0.1:8000/api/vi/books 
    path('vi/books/', views.book_list, name='book_list'),
    

]
