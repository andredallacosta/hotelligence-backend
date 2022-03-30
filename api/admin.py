from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import (
    Guest, Hotel, Room, RoomType, User, Address, Phone, Booking
)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ('id', 'email', 'hotel', 'created_at', 'updated_at')
    search_fields = ('id', 'email', 'hotel__id', 'hotel__name')


class AdminHotel(admin.ModelAdmin):
    model = Hotel
    list_display = ('id', 'name', 'site', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'site')


class AdminPhone(admin.ModelAdmin):
    model = Phone
    list_display = ('id', 'ddi', 'ddd', 'number', 'created_at', 'updated_at')
    search_fields = ('id', 'ddi', 'ddd', 'number')


class AdminAddress(admin.ModelAdmin):
    model = Address
    list_display = ('id', 'address1', 'address2', 'district', 'city', 'state',  'country', 'cep', 'number', 'created_at', 'updated_at')
    search_fields = ('id', 'address1', 'address2', 'district', 'city', 'state',  'country', 'cep', 'number')


class AdminGuest(admin.ModelAdmin):
    model = Guest
    list_display = ('id', 'first_name', 'last_name', 'cpf', 'rg', 'email', 'created_at', 'updated_at')
    search_fields = ('id', 'first_name', 'last_name', 'cpf', 'rg', 'email')


class AdminRoom(admin.ModelAdmin):
    model = Room
    list_display = ('id', 'type', 'number', 'value', 'status', 'hotel', 'created_at', 'updated_at')
    search_fields = ('id', 'type', 'number', 'value', 'status', 'hotel__id', 'hotel__name')


class AdminRoomType(admin.ModelAdmin):
    model = RoomType
    list_display = ('id', 'type', 'capacity', 'double_bed_quantity', 'single_bed_quantity', 'bathroom_quantity', 'air_conditioning', 'fridge', 'balcony', 'created_at', 'updated_at')
    search_fields = ('id', 'type', 'capacity')


class AdminBooking(admin.ModelAdmin):
    model = Booking
    list_display = ('id', 'room', 'guest', 'guest_quantity', 'daily_value', 'check_in', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('id', 'room__id', 'room__type', 'room__number', 'room__value', 'room__status', 'room__hotel__id', 'room__hotel__name', 'guest__id', 'guest__first_name', 'guest__last_name', 'guest__cpf', 'guest__rg', 'guest__email', 'guest_quantity', 'daily_value', 'check_in', 'start_date', 'end_date')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Hotel, AdminHotel)
admin.site.register(Phone, AdminPhone)
admin.site.register(Address, AdminAddress)
admin.site.register(Guest, AdminGuest)
admin.site.register(Room, AdminRoom)
admin.site.register(RoomType, AdminRoomType)
admin.site.register(Booking, AdminBooking)
