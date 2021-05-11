from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from login.views import *

urlpatterns = [
    url(r'^v1/auth/$', AuthView.as_view()),
]
router = SimpleRouter()
urlpatterns += router.urls