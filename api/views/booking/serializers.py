from rest_framework import serializers
from api.models import (
    Booking,
)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
