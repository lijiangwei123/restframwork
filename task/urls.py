from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^v1/$', views.task_list, name='task_list'),
    # url(r'^v1/$', views.TaskListCreate.as_view(), name='task_list'),
    url(r'^v1/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
]