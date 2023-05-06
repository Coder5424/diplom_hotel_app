from django.urls import path
from .views import CheckInView, GetDataView, GetExcelView
from . import views

urlpatterns = [
    path(
        'checkin/<firstname>/<lastname>/<email>/<phone_number>/<room>/<check_in>/<check_out>',
        CheckInView.as_view(),
        name='CheckInView'
    ),
    path('admin_booking_list/', views.admin_booking_list, name='admin_booking_list'),
    path('admin_page/', views.admin_page_view, name='admin_page_view'),
    path('search_bookings/', views.search_bookings_view, name='search_bookings_view'),
    path('get_data/', GetDataView.as_view(), name='GetDataView'),
    path('get_excel/', GetExcelView.as_view(), name='GetExcelView'),

]