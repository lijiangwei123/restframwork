class Request:
    def __init__(self, obj):
        self.obj = obj

    @property # 调用的时候不用再去添加()
    def user(self):
        return self.obj.authticate()

class Auth:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def authticate(self):
        return self.name

class APIView:

    def f2(self):
        # 第三步 实例化Auth类的对象
        auth = Auth('alex', 19)
        # 第四步 实例化Request类的对象
        res = Request(auth)
        print(res.user, "ppppppppppppppppp")
# 第一步
obj = APIView()
# 第二步
obj.f2()
