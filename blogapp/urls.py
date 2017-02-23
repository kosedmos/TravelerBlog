from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^articles/$', views.article_list),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.article_detail),
]
