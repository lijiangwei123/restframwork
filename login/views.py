from django.shortcuts import render
import time
from login import models
from django.http import JsonResponse
from rest_framework.views import APIView
from utils.get_token import get_token
# Create your views here.

class AuthView(APIView):
    authentication_classes = {}

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            # 参数是datadict格式
            user = request.data.get('username')
            pas = request.data.get('password')
            obj = models.User.objects.filter(username=user, password=pas).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或者密码有误'
                return JsonResponse(ret)
            payload = {
                "id": obj.id,
                'name': obj.username
            }
            token = get_token(payload, 10)
            ret['msg'] = '登陆成功'
            data = {}
            data['token'] = token
            ret['data'] = data
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)
