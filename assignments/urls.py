from django.conf.urls import url, include

from .import views

urlpatterns = [

    url(r'^$',views.assignment_list, name='list'),
    url(r'^(?P<slug>[-\w]+)/$', views.assignment_detail, name='detail'),

]
