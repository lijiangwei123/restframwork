from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication

class MyAuthentication(BasicAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        if(token  == '123'):
            user = 'zhangsan'
        else:
            user  = 'lijiangwei'
        return (user, None)

    def authenticate_header(self, val):
        return 'Basic realm="api"'
