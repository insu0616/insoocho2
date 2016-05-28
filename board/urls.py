from django.conf.urls import url
from . import views

app_name = 'board'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail')
]



