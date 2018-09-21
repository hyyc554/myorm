from django.shortcuts import render, HttpResponse
from app01.models import Book, Publish, Author, AuthorDetail


# Create your views here.
# def index(request):
#     # 创建数据
#     # Book.objects.create(title="python葵花宝典", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
#     # Book.objects.create(title="代码", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
#     # Book.objects.create(title="重构", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
#     # print(Book.objects.filter(title='代码').all().values('title'))
#     # 1 查询老男孩出版社出版过的价格大于200的书籍
#     # book_list = Book.objects.filter(publish='老男孩出版社', price__gt=200).all().values('title')
#     # 2 查询2017年8月出版的所有以py开头的书籍名称
#     # book_list = Book.objects.filter(pub_date__year=2017,pub_date__month=8,title__startswith='py').all().values('title')
#     # 3 查询价格为50,100或者150的所有书籍名称及其出版社名称
#     # book_list = Book.objects.filter(price__in=(50, 100, 150)).all().values_list('title','publish')
#
#     # 4 查询价格在100到200之间的所有书籍名称及其价格
#     # book_list = Book.objects.filter(price__range=(100,200)).all().values_list('title','price')
#
#     # 5 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
#     book_list = Book.objects.filter(publish='人民出版社').all().values_list('title','price').distinct()
#
#
#     print(book_list)
#
#     return HttpResponse('ok')

def index(request):
    # book_obj = Book.objects.filter(pk=1).first()
    # print(book_obj.publish.city)
    # publish = Publish.objects.filter(name='科学出版社').first()
    # book_list = publish.book_set.all().values('title')
    # print(book_list)
    # tom = Author.objects.filter(name='tom').first()
    # bl =tom.authorDetail.telephone
    bl=Book.objects.filter(publish__name='科学出版社').values_list('title','publish__name')
    print(bl)
    return HttpResponse('OK')
