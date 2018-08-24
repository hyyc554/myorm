from django.shortcuts import render, redirect, HttpResponse
from app01.models import *

import random


# Create your views here.

def start(request):
    """
    数据初始化的视图函数
    :param request:
    :return: 若创建成功将会访问首页
    """
    aut_list = [('tom', 22), ('mark', 23), ('jack', 24)]
    for aut in aut_list:
        aut_obj = Author.objects.create(name=aut[0], age=aut[1])
    pub_list = [('人民出版社', 'beijing', 'renming@qq.com'), ('机械工业出版社', 'nanjing', 'gongye@qq.com'),
                ('科学出版社', 'wuhan', 'science@qq.com')]
    for pub in pub_list:
        pub_obj = Publish.objects.create(name=pub[0], city=pub[1], email=pub[2])
    book_list = [('追风筝的人', 200, '2012-11-12', 1), ('python', 123, '2012-11-12', 2), ('html', 234, '2012-11-13', 2),
                 ('go', 122, '2011-11-12', 3), ]
    for book in book_list:
        book_obj = Book.objects.create(title=book[0], price=book[1], pub_date=book[2], publish_id=book[3])
        book_aut1 = Author.objects.filter(name=aut_list[random.randint(0, 2)][0]).first()
        book_aut2 = Author.objects.filter(name=aut_list[random.randint(0, 2)][0]).first()
        book_obj.authors.add(book_aut1, book_aut2)
    return redirect('app01:books')


def add_book(request):
    """
    添加书籍信息的视图函数
    :param request:
    :return:
    """
    if request.POST:
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        authors = request.POST.getlist('authors')
        book_obj = Book.objects.create(title=title, price=price, pub_date=date, publish_id=publish)
        book_obj.authors.add(*authors)
        return redirect('app01:books')

    pub_list = Publish.objects.all()
    aut_list = Author.objects.all()

    return render(request, 'add_book.html', {'pub_list': pub_list, 'aut_list': aut_list})


def mod_book(request, id):
    mod_obj = Book.objects.filter(nid=id).first()
    if request.POST:
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        authors = request.POST.getlist('authors')
        Book.objects.filter(pk=id).update(title=title, price=price, pub_date=date, publish_id=publish)
        mod_obj.authors.set(authors)
        return redirect('app01:books')

    pub_list = Publish.objects.all()
    aut_list = Author.objects.all()
    return render(request, 'modbook.html', {'mod_obj': mod_obj, 'pub_list': pub_list, 'aut_list': aut_list})


def books(request):
    book_list = Book.objects.all()

    return render(request, 'books.html', {'book_list': book_list})


def del_book(request, id):
    Book.objects.filter(nid=id).delete()
    return redirect('app01:books')


def aut_detail(request, id, tag):
    if tag == "2":
        print(id)
        book_list = Book.objects.filter(authors__nid=id).all()
    else:
        book_list = Book.objects.filter(publish_id=id).all()
    return render(request, 'book_detail.html', locals())
