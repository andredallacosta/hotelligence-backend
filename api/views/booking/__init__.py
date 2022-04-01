from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api.models import Booking
from .serializers import (
    BookingSerializer,
)


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BookingSerializer
