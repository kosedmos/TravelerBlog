from django.conf.urls import url
'''Поддержка разных форматов передачи данных'''
from rest_framework.urlpatterns import format_suffix_patterns
from blogapp import views

urlpatterns = [
    url(r'^articles/$', views.ArticleList.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)