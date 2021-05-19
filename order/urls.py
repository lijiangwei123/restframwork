from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^v1/$', views.OrderView.as_view(), name='order'),
    url(r'^v1/dog/$', views.DogView.as_view(), name='dog')
]