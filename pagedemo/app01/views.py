from django.shortcuts import render
from app01.models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    """
    批量建表
    book_list = []
    for i in range(100):
        book = Book(title='book_%s'%i,price=i*i)
        book_list.append(book)
    Book.objects.bulk_create(book_list)
    """
    book_list = Book.objects.all()
    paginator= Paginator(book_list,8)
    print('count:',paginator.count)
    print('num_pages:',paginator.num_pages)
    print('page_range',paginator.page_range)

    current_page_num = int(request.GET.get('page',1))


    return render(request,'index.html')