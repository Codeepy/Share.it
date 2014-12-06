from django.conf.urls import patterns, include, url
from django.contrib import admin

from foodbank import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^donation/', views.about, name='donation'),
    url(r'^api/', views.api, name='api'),
    url(r'^map/', views.map, name='map'),
)
