from django.conf import urls
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from modules.userService.views import UserModelResource
from modules.userService.api import router
from modules.userService.api import UserListView

urlpatterns = patterns('',
    url(r'^login/', 'modules.userService.views.makeUserLogin', name='login'),
    url(r'^loginCheck/', 'modules.userService.views.loginCheck', name='loginCheck'),

    # Tastypie
    url(r'^v1/', urls.include(UserModelResource().urls)),

    # DjangoRestful Framework
    url(r'^v2/', include(router.urls)),

    url(r'^v3/userList/(?P<username>.+)/$', UserListView.as_view()),
    url(r'^v3/userList/$', UserListView.as_view()),
)
