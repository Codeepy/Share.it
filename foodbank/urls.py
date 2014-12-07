from django.conf.urls import patterns, include, url
from django.contrib import admin

from foodbank import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', views.about, name='about'),
    url(r'^home/', views.home, name='home'),
    url(r'^home/', views.home, name='contact'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^donation/', views.donation, name='donation'),
    url(r'^donation/', views.about, name='donation'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^api/', views.api, name='api'),
    url(r'^map/', views.map, name='map'),

    url(r'^broadcast/', 'chat.views.broadcast', name='broadcast'),
    url(r'^notifications/', 'chat.views.notifications', name='notifications'),
    url(r'^accounts/registeruser', 'chat.views.register_user', name='register_user'),
    url(r'^accounts/registerfoodbank', 'chat.views.register_foodbank', name='register_foodbank'),
    url(r'^accounts/register', 'chat.views.register', name='register'),
    url(r'^accounts/login', 'chat.views.login_user', name='login_user'),
    url(r'^accounts/logout/', 'chat.views.logout_user', name='logout_user'),
)
