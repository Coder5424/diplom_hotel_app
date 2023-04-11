from django.urls import path
from . import views
from .views import BookingView, RoomDetailView, room_list_view

urlpatterns = [
    path('', room_list_view, name='room_list_view'),
    path('booking/', BookingView.as_view(), name='BookingView'),
    path('room/<type>', RoomDetailView.as_view(), name='RoomDetailView')
]
