from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import (
    Hotel,
)
from api.exceptions import (
    UserHasNoHotel,
)
from .serializers import (
    HotelSerializer,
    HotelPopulatedSerializer
)


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = HotelSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelPopulatedSerializer
        if self.action == 'retrieve':
            return HotelPopulatedSerializer
        if self.action == 'get_bookings':
            return HotelPopulatedSerializer
        return HotelSerializer

    @action(detail=True, methods=['get'])
    def get_hotel_by_user(self, request, pk=None):
        try:
            instance = Hotel.objects.get(users__id=request.user.id)
        except Hotel.DoesNotExist:
            raise UserHasNoHotel
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
