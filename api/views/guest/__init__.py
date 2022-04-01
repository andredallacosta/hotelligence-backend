from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api.models import Guest
from .serializers import (
    GuestSerializer,
    GuestPopulatedSerializer,
)


class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = GuestSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return GuestPopulatedSerializer
        if self.action == 'retrieve':
            return GuestPopulatedSerializer
        return GuestSerializer
