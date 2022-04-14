from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.exceptions import TokenDoesNotExist


class AuthLoginViewSet(ObtainAuthToken):

    def get_object(self, token):
        try:
            return Token.objects.get(key=token)
        except Token.DoesNotExist:
            raise TokenDoesNotExist

    def get(self, request, *args, **kwargs):
        token = self.get_object(request.GET.get('token', ''))

        return Response({
            'token': token.key,
            'id': token.user.id,
            'email': token.user.email
        })

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email
        })
