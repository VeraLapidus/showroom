from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
