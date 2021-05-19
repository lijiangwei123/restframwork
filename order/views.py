from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views import View
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
import json


# Create your views here.

@method_decorator(csrf_exempt, name = 'dispatch')
class OrderView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('获取订单')

    def post(self, request, *args, **kwargs):
        return HttpResponse('创建订单')

    def put(self, request, *args, **kwargs):
        return HttpResponse('更新订单')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除订单')

class MyAuthentication:
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return ('alex', None)

    def authenticate_header(self, val):
        pass


class DogView(APIView):
    authentication_classes = [MyAuthentication,]
    def get(self, request, *args, **kwargs):
        self.dispatch()
        ret = {
            'code': 1,
            'msg': '操作成功'
        }
        return HttpResponse(json.dumps(ret))

    def post(self, request, *args, **kwargs):
        return HttpResponse('创建订单')

    def put(self, request, *args, **kwargs):
        return HttpResponse('更新订单')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除订单')