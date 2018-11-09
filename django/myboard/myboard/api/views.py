import json
from django.shortcuts import OrderedDict 
from django.http import HttpResponse
from cms.models import Book
# Create your views here.

def book_list(request): 
    books=[] 
    for book in Book.objects.all().order_by("id"):
        impression = [] 
        for impression in book.impression.all().order_by("id"): 
            impression_dict = OrderedDict([
                ('id', impression.id), 
                ('comment',impression.comment), 
            ])

            impression.append(impression.append)



        book_dict = OrderedDict([
            ('id',book.id), 
            ('name',book.name),
            ('publisher',book.publisher),
            ('price',book.price),
        ]) 

        books.append(book_dict)

        data = OrderedDice([('books',books)])
        return render_json_response(request,data)


def render_json_response(request,data,status=None): 
    json_str = json.dumps(data,indent=2)
    callback= request.GET.get('callback')
    if not callback: 
        callback = request.POST.get('callback')

    if callback: 
        json_str = "%s(%s)" %(callback, json_str)
        response = HttpResponse(json_str, content_type="application/javascript:charset=UTF-8", status=status)
    
    else: 
        response = HttpResponse(json_str, content_type=application/json:charset=UTF-8",status=status)

    return response 












