from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from bookmark.models import Bookmark
# Create your views here.
from myweb.views import LoginRequiredMixin
from django.urls import reverse_lazy 



class BookmarkLV(ListView): 
    #object_list 
    #views.py => template (xxxx.html)

    model = Bookmark 

class BookmarkDV(DetailView): 
    # object 
    # views.py => template (xxxx_detail.html)

    model = Bookmark 

class BookmarkCreateView(LoginRequiredMixin,CreateView): 

    model =Bookmark 
    fields=['title','url','url_category']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)




class BookmarkChangeLV(LoginRequiredMixin,ListView): 

    template_name = "bookmark/bookmark_change_list.html"

    def get_queryset(self): #전체 리스트 다 가져오면 안돼.
        
        return Bookmark.objects.filter(owner = self.request.user)
        
    



class BookmarkUpdateView(LoginRequiredMixin,UpdateView):

    model=Bookmark 
    fields= ['title','url','url_category']
    success_url = reverse_lazy('bookmark:index')



class BookmarkDeleteView(LoginRequiredMixin,DeleteView):

    model=Bookmark 
    success_url = reverse_lazy('bookmark:index')






