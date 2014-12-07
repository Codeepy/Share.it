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

    url(r'^broadcast/', 'share_it.views.broadcast', name='broadcast'),
    url(r'^notifications/', 'share_it.views.notifications', name='notifications'),
    url(r'^accounts/registeruser', 'share_it.views.register_user', name='register_user'),
    url(r'^accounts/registerfoodbank', 'share_it.views.register_foodbank', name='register_foodbank'),
    url(r'^accounts/register', 'share_it.views.register', name='register'),
    url(r'^accounts/login', 'share_it.views.login_user', name='login_user'),
    url(r'^accounts/logout/', 'share_it.views.logout_user', name='logout_user'),
)
