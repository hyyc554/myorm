from django.shortcuts import render, HttpResponse
from app01.models import Book


# Create your views here.
def index(request):
    # 创建数据
    # Book.objects.create(title="python葵花宝典", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
    # Book.objects.create(title="代码", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
    # Book.objects.create(title="重构", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
    print(Book.objects.filter(title='代码').all().values('title'))
    return HttpResponse('ok')
