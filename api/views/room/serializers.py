from rest_framework import serializers
from api.models import (
    Booking, Room, Hotel, RoomType,
)


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class RoomPopulatedSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = '__all__'
