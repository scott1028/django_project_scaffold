# coding: utf-8
# ref: https://docs.djangoproject.com/en/1.8/topics/auth/default/#how-to-log-a-user-in
# ref: http://stackoverflow.com/questions/5376985/django-request-user-is-always-anonymous-user

# from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from modules.daoService.models import User


# Create your views here.
@require_POST
def makeUserLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    # deprecated
    # user = authenticate(username=username, password=password)
    user = User.objects.get(username=username, password=password)

    if user is not None:
        if user.is_active:
            # update session
            login(request, user)
            # Redirect to a success page.

            return HttpResponse(status=200)
        else:
            # Return a 'disabled account' error message
            # ...
            return HttpResponse(status=401)
    else:
        # Return an 'invalid login' error message.
        # ...
        return HttpResponse(status=401)


def loginCheck(request):
    print request.user.is_anonymous()
    return HttpResponse(request.user.pk, status=200)


# ref: http://stackoverflow.com/questions/22510756/pendingdeprecationwarning-on-django-tastypie
# tastypie django 1.8 issue
from tastypie import resources
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS  # noqa

class UserModelResource(resources.ModelResource):
    username = fields.CharField(attribute='username',
                 readonly=True)  # 不允許修改

    # roles = fields.OneToManyField(
    #     'modules.daoService',
    #     'user.book_set',
    #     null=True
    # )

    class Meta:
        queryset = User.objects.all()  # noqa, fix issue ssd-173
        resource_name = 'user'
        list_allowed_methods = ['get']
        # detail_allowed_methods = ['get', 'patch', 'delete']
        excludes = ['pk']
        always_return_data = True
        # update setting
        # authentication = authentication.WebClientAuthentication()
        # authorization = Authorization()
        filtering = {
            'username': ALL
        }