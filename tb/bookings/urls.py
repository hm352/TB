from django.urls import path

from .views import Homepage, BookingView

urlpatterns = [
    path('', Homepage, name='homepage'),
    path('bookings/',BookingView.as_view() , name = 'booking_form')
]