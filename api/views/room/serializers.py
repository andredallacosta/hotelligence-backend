from rest_framework import serializers
from api.models import (
    Booking, Guest, Room, Hotel, RoomType,
)


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Guest
        fields = '__all__'

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class BookingPopulatedSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()

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
    bookings = BookingPopulatedSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'
