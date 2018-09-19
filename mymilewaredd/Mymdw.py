# -*- coding: utf-8 -*-

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Md1(MiddlewareMixin):

    def process_request(self, request):
        print("Md1请求")

    def process_response(self, request, response):
        print('Md1返回')
        return response
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("Md1view")
        # response=callback(request,*callback_args,**callback_kwargs)
        # return response
    def process_exception(self,request, exception):
        print("md1 process_exception...")

class Md2(MiddlewareMixin):

    def process_request(self, request):
        print("Md2请求")
        # return HttpResponse("Md2中断")

    def process_response(self, request, response):
        print("Md2返回")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("Md2view")
        # response = callback(request, *callback_args, **callback_kwargs)
        # return response
    def process_exception(self,request, exception):
        print("md2 process_exception...")
        return HttpResponse("error")

