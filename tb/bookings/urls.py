from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('booking', views.booking, name = 'booking_form')
]