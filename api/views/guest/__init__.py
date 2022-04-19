from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
import copy

from api.models import Address, Guest, Phone
from api.exceptions import (
    CheckWithNoParam,
    GuestDoesNotExist,
    GuestAlreadyExists
)
from .serializers import (
    GuestSerializer,
    GuestPopulatedSerializer,
    PhoneSerializer,
    AddressSerializer
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

    def create(self, request, *args, **kwargs):
        data = copy.deepcopy(request.data)

        if 'phone' in data:
            try:
                instance = Phone.objects.get(id=data['phone']['id'])
                serializer = PhoneSerializer(instance, data=data['phone'])
            except:
                serializer = PhoneSerializer(data=data['phone'])

            if serializer.is_valid(raise_exception=True):
                phone = serializer.save()
                data['phone'] = phone.id

        if 'address' in data:
            try:
                instance = Address.objects.get(id=data['address']['id'])
                serializer = AddressSerializer(instance, data=data['address'])
            except:
                serializer = AddressSerializer(data=data['address'])

            if serializer.is_valid(raise_exception=True):
                address = serializer.save()
                data['address'] = address.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = copy.deepcopy(request.data)

        if 'phone' in data:
            try:
                instance = Phone.objects.get(id=data['phone']['id'])
                serializer = PhoneSerializer(instance, data=data['phone'])
            except:
                serializer = PhoneSerializer(data=data['phone'])

            if serializer.is_valid(raise_exception=True):
                phone = serializer.save()
                data['phone'] = phone.id

        if 'address' in data:
            try:
                instance = Address.objects.get(id=data['address']['id'])
                serializer = AddressSerializer(instance, data=data['address'])
            except:
                serializer = AddressSerializer(data=data['address'])

            if serializer.is_valid(raise_exception=True):
                address = serializer.save()
                data['address'] = address.id

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def check(self, request, format=None):
        email = request.GET.get('email', None)
        if not email:
            raise CheckWithNoParam

        try:
            self.queryset.get(email=email)
        except Guest.DoesNotExist:
            raise GuestDoesNotExist

        raise GuestAlreadyExists
