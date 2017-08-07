"""Define URL patterns for posts"""
from django.conf.urls import url
from . import views
urlpatterns = [

    #Home page
    url(r'^$',views.index,name='index'),
    url(r'^posts/$', views.BlogListView.as_view(), name='blog-list'),
    url(r'^post/(?P<slug>[-\w\d]+)', views.post, name='post')
]
