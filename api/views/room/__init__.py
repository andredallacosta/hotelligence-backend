from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import (
    Room, Booking,
)
from .serializers import (
    RoomSerializer,
    RoomPopulatedSerializer,
    BookingSerializer,
)


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = RoomSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return RoomPopulatedSerializer
        if self.action == 'retrieve':
            return RoomPopulatedSerializer
        if self.action == 'get_bookings':
            return BookingSerializer
        return RoomSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(hotel=request.user.hotel)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_bookings(self, request, pk=None):
        queryset = Booking.objects.filter(room=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
