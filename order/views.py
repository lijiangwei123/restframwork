from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views import View
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
import json


# Create your views here.


@method_decorator(csrf_exempt, name = 'dispatch')
class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('获取订单')

    def post(self, request, *args, **kwargs):
        return HttpResponse('创建订单')

    def put(self, request, *args, **kwargs):
        return HttpResponse('更新订单')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除订单')


class DogView(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        self.dispatch()
        print(request.user)
        ret = {
            'code': 1,
            'msg': '操作成功'
        }
        return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        ret1 = {
            'code': 1,
            'msg': '创建订单'
        }
        return JsonResponse(ret1)

    def put(self, request, *args, **kwargs):
        return HttpResponse('更新订单')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除订单')


