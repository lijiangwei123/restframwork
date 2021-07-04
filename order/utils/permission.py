from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    message = "只有李江伟才能访问"
    def has_permission(self, request, view):
        if(request.user == 'zhangsan'):
            return False
        return True
