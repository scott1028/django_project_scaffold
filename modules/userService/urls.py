from django.conf import urls
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from modules.userService.views import UserModelResource

urlpatterns = patterns('',
    url(r'^login/', 'modules.userService.views.makeUserLogin', name='login'),
    url(r'^loginCheck/', 'modules.userService.views.loginCheck', name='loginCheck'),
    url(r'', urls.include(UserModelResource().urls))
)
