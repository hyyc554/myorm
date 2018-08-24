from django.shortcuts import render, HttpResponse

from app01.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def test(request):
    return HttpResponse('hello Ajax')


def cal(request):
    print(request.POST)
    n1 = int(request.POST.get('n1'))
    n2 = int(request.POST.get('n2'))
    ret = n1 + n2
    return HttpResponse(ret)


def login(request):
    print(request.POST)
    user = request.POST.get("user")
    pwd = request.POST.get('pwd')
    user = User.objects.filter(name=user, pwd=pwd).first()
    res = {"user": None, "msg": None}
    if user:
        res["user"] = user.name
    else:
        res["msg"] = "username or password wrong!"
    import json
    return HttpResponse(json.dumps(res))
