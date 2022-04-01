from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api.models import RoomType
from .serializers import (
    RoomTypeSerializer,
)


class RoomTypeViewSet(ModelViewSet):
    queryset = RoomType.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = RoomTypeSerializer
