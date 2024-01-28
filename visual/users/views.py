from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import User
from .serializers import UserSerializer
from .permissions import IsUserOrAdmin


class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return (IsAuthenticatedOrReadOnly(),)
        return (IsUserOrAdmin(),)
