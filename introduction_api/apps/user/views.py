from rest_framework import viewsets

from introduction_api.apps.user.models import User
from introduction_api.apps.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = (
        'get',
        'post',
        'patch',
        'delete',
    )
