"""Define URL patterns for posts"""
from django.conf.urls import url
from . import views
urlpatterns = [

    #Home page
    url(r'^$',views.index,name='index'),
    url(r'^entries/$', views.EntryListView.as_view(), name='entry-list'),
    url(r'^entry/(?P<slug>[-\w\d]+)', views.entry, name='entry'),
    url(r'^create/',views.create, name='create'),
    url(r'^edit/(?P<slug>[-\w\d]+)', views.edit, name='edit')
]
