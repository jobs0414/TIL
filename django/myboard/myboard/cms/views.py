from django.shortcuts import render, get_object_or_404, redirect  #내꺼
from django.http import HttpResponse
from cms.models import Book, Impression
from cms.forms import BookForm,ImpressionForm
from django.views.generic.list import ListView

# Create your views here.
def book_list(request):
    # return HttpResponse('도서 목록')
    books = Book.objects.all().order_by('id')

    context = {}
    context['books'] = books

    return render(request, 'cms/book_list.html', context)

def book_edit(request, book_id=None):
    # return HttpResponse('도서 수정')
    
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()
    
    if request.method == 'POST': # POST
        # POST된 request 데이터를 가지고 Form 생성
        form = BookForm(request.POST, instance=book) 
        # save()
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list') #단순히 페이지 요청만 필요하다. request정보 안가지고 감. 

    else: # GET 
        # book instance에서 Form 생성
        form = BookForm(instance=book) 
        return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))



def book_remove(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete() 
    return redirect('cms:book_list')

class ImpressionList(ListView):
    context_object_name = "impressions"
    template_name = "cms/impression_list.html"
    paginate_by = 2 



    def get(self,request,*args,**kwargs):
        book = get_object_or_404(Book,pk=kwargs["book_id"])
        impressions= book.impressions.all().order_by("id") 
        self.object_list = impressions 

        context = self.get_context_data(object_list=self.object_list, book=book)
        return self.render_to_response(context)


def impression_edit(request,book_id, impression_id=None):
    book = get_object_or_404(Book,pk=book_id)
    if impression_id:
        impression = get_object_or_404(Impression,pk=impression_id)


    else:
        impression = Impression()


    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)
        # save()
        if form.is_valid():
            impression = form.save(commit=False)
            impression.book = book
            impression.save()
            return redirect('cms:impression_list',book_id=book_id)  # 단순히 페이지 요청만 필요하다. request정보 안가지고 감.

        #DB반영 작업


        else:
            form = ImpressionForm(instance=impression)

        return render(request,'cms/impression_edit.html', dict(form=form, book_id=book_id, impression_id=impression_id))
        #화면에 View작업




def impression_remove(request,book_id, impression_id):
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list',book_id=book_id)



