from rest_framework import serializers
from api.models import (
    Phone, Address, Guest
)


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Guest
        fields = '__all__'

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class GuestPopulatedSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phone = PhoneSerializer()
    address = AddressSerializer()

    class Meta:
        model = Guest
        fields = '__all__'

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)
