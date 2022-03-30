from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    hotel = models.ForeignKey('Hotel', related_name='users', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone = models.ForeignKey('Phone', related_name='hotels', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.ForeignKey('Address', related_name='hotels', null=True, blank=True, on_delete=models.SET_NULL)
    site = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(
            self.id,
            self.name
        )


class Phone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ddi = models.CharField(max_length=5, default='+55')
    ddd = models.CharField(max_length=2, null=True, blank=True)
    number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, ({}) {}".format(
            self.id,
            self.ddd,
            self.number
        )


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    number = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(
            self.id,
            self.address1,
            self.city,
            self.state,
            self.country,
            self.number,
        )


class Guest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    rg = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.ForeignKey('Phone', related_name='guests', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.ForeignKey('Address', related_name='guests', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}, {}".format(
            self.id,
            self.email,
            self.first_name,
        )


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey('RoomType', related_name='rooms', null=True, blank=True, on_delete=models.SET_NULL)
    number = models.IntegerField()
    value = models.FloatField()
    status = models.CharField(max_length=20, null=True, blank=True)
    hotel = models.ForeignKey('Hotel', related_name='rooms', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(
            self.id,
            self.number,
        )


class RoomType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField(null=True, blank=True)
    double_bed_quantity = models.IntegerField(null=True, blank=True)
    single_bed_quantity = models.IntegerField(null=True, blank=True)
    bathroom_quantity = models.IntegerField(null=True, blank=True)
    air_conditioning = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(
            self.id,
            self.type,
        )


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey('Room', related_name='bookings', on_delete=models.CASCADE)
    guest = models.ForeignKey('Guest', related_name='bookings', on_delete=models.CASCADE)
    guest_quantity = models.IntegerField()
    daily_value = models.FloatField()
    extras_value = models.FloatField(null=True, blank=True)
    paid_value = models.FloatField(null=True, blank=True)
    check_in = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}, {}".format(
            self.id,
            self.room,
            self.guest,
        )