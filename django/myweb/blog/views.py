from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView,TodayArchiveView,DayArchiveView

from blog.models import Post
# Create your views here.
from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q

class PostLV(ListView): 
    model = Post 
    template_name = 'blog/post_all.html'  #post_list.html 
    context_object_name = 'posts' #object_list
    paginate_by= 4 

class PostDV(DetailView):
    model = Post 


class PostAV(ArchiveIndexView): 
    model = Post 
    date_field = 'modify_date'
   

class PostYAV(YearArchiveView): 
    model = Post 
    date_field = 'modify_date'
    make_object_list = 'True'


class PostMAV(MonthArchiveView): 
    model = Post 
    date_field = 'modify_date'


class PostDAV(DayArchiveView): 
    model = Post 
    date_field = 'modify_date'



class PostTAV(TodayArchiveView): 
    model = Post 
    date_field = 'modify_date'


class SearchFormView(FormView):
    form_class = PostSearchForm  #form.py에 생성 
    template_name = "blog/post_search.html"
    print("TEST")

    def form_valid(self,form): #self.request 
        schWord = '%s' % self.request.POST['search_word']
        print("key=" + schWord)
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        print("list size=" + str(len(post_list)))

        context={} 
        context['form'] = form 
        context['search_keyword'] = schWord
        context['search_list'] = post_list 

        return render(self.request , self.template_name, context)







