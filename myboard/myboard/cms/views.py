from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from cms.models import Book,Impression
from cms.forms import BookForm,ImpressionForm


# Create your views here.

def book_list(request): 

    books = Book.objects.all().order_by('id')

    context = {} 
    context['books']= books 
    
    return render(request, 'cms/book_list.html',context)


def book_edit(request,book_id=None): 

    if book_id: 
        book = get_object_or_404(Book, pk=book_id)

    else:
        book=Book()

    if request.method == 'POST': 
        form = BookForm(request.POST, instance=book) # Post된 request 데이터를 가지고 Form 생성 
        #save()
        if form.is_valid(): 
            book = form.save(commit=False)
            book.save() 
            return redirect('cms:book_list')


    else: 
        form = BookForm(instance=book) 
        return render(request, 'cms/book_edit.html',dict(form=form, book_id=book_id))


def book_remove(request,book_id): 
    return HttpResponse('도서 삭제')


