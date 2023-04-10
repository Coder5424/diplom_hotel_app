from django.urls import path
from . import views
from .views import BookingView

urlpatterns = [
    path('booking/', BookingView.as_view(), name='booking_view'),
]
