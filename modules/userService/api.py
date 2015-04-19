# coding: utf-8
# ref: http://www.django-rest-framework.org/#installation
# ref: http://www.django-rest-framework.org/api-guide/filtering/#filtering-against-query-parameters
# ref: http://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends


from django.conf.urls import url, include
from modules.daoService.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import filters
from rest_framework.response import Response


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    # def list(self, request):
    #     print self.request.QUERY_PARAMS
    #     username = self.request.QUERY_PARAMS.get('username', None)
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)

from rest_framework import generics

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.kwargs.get('username', None) or self.request.QUERY_PARAMS.get('username', None)
        filters = {}
        if username is not None:
            filters['username'] = username
        return User.objects.filter(**filters)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# from rest_framework import generics


# class UserList(generics.ListAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         return User.objects.filter(username='1')

# router.register(r'users2', UserList)
