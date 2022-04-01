from django.urls import path
from .views import (
    RoomViewSet, RoomTypeViewSet, BookingViewSet, GuestViewSet
)


list_mapping = {'get': 'list', 'post': 'create'}
detail_mapping = {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}

app_name = 'api'
urlpatterns = [
    path('room', RoomViewSet.as_view(list_mapping), name='room_list'),
    path('room/<pk>', RoomViewSet.as_view(detail_mapping), name='room_detail'),
    path('room/<pk>/booking', RoomViewSet.as_view({'get': 'get_bookings'}), name='room_booking'),

    path('room_type', RoomTypeViewSet.as_view(list_mapping), name='room_type_list'),
    path('room_type/<pk>', RoomTypeViewSet.as_view(detail_mapping), name='room_type_detail'),

    path('booking', BookingViewSet.as_view(list_mapping), name='booking_list'),
    path('booking/<pk>', BookingViewSet.as_view(detail_mapping), name='booking_detail'),

    path('guest', GuestViewSet.as_view(list_mapping), name='guest_list'),
    path('guest/<pk>', GuestViewSet.as_view(detail_mapping), name='guest_detail'),
]
