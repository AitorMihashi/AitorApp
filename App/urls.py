'''
Created on 3/9/2014

@author: pedro
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('App.views',
    url(r'^series/$', 'Series_list'),
)