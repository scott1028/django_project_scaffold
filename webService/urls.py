from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webService.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^userService/', include('modules.userService.urls')),

	# If you're intending to use the "browsable API",
	# you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
