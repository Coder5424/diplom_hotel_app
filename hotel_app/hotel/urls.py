from django.urls import path
from . import views
from .views import BookingView, RoomDetailView

urlpatterns = [
    path('', views.room_list_view, name='room_list_view'),
    path('booking/', BookingView.as_view(), name='BookingView'),
    path('room/<type>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking_list/', views.booking_list_view, name='booking_list_view'),
    path('error_booking/', views.error_booking, name='error_booking'),
    path('error_date/', views.error_date, name='error_date'),
    path('data/', views.data_handler, name='data-handler'),
]
