from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView,TodayArchiveView,DayArchiveView

from blog.models import Post
# Create your views here.
from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q

from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from myweb.views import LoginRequiredMixin

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

class PostCreateView(LoginRequiredMixin,CreateView):

    model =Post 
    fields = ['title','slug','description','content']
    intial = {'slug','auto-filling-by-title'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self,form): 
        self.instance.owner = self.request.user
        return super(PostCreateView,self).form_valid(form)
        

class PostChangeLV(LoginRequiredMixin,ListView):

    template_name = "blog/blog_change_list.html"

    def get_queryset(self): #필터링 해서 가져오면 된다. 
        Post.objects.filter(owner = self.request.user)
        return super().get_queryset()


class PostUpdateView(LoginRequiredMixin,UpdateView):

    model =Post 
    fields = ['title','slug','description','content']
    success_url = reverse_lazy('blog:index')


class PostDeleteView(LoginRequiredMixin,DeleteView):

    model =Post 
    success_url = reverse_lazy('blog:index')
    








