from rest_framework import serializers
from api.models import (
    Address, Phone, Hotel,
)


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelPopulatedSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()
    address = AddressSerializer()

    class Meta:
        model = Hotel
        fields = '__all__'
