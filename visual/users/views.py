from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users import serializers
from users.models import User
from users.permissions import IsOwnerOrAdmin
from users.serializers import UserSerializer


class UserViewSet(DjoserUserViewSet):
    """
        Вьюсет для пользователей. Можно получить список пользователей и пользователя
        по id без авторизации. Все действия над пользователем доступны только
        создателю профиля или админу. Также есть роутер users/me/ для удобства
        действия над своим профилем.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsOwnerOrAdmin()]

    @action(
        detail=False,
        permission_classes=[IsOwnerOrAdmin],
        methods=['GET', 'PATCH', 'DELETE', 'PUT']
    )
    def me(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)
        user = request.user

        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)

        elif request.method in ['PATCH', 'PUT']:
            serializer = serializers.UserSerializer(
                user,
                data=request.data,
                partial=request.method == 'PATCH'
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            user.delete()
            return Response(
                {"detail": "Профиль успешно удален"},
                status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
