from django.shortcuts import render
from .models import User, Booking
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 

from django.views.generic.edit import CreateView


def Homepage(request):
	return render(request, 'bookings/index.html')

class BookingView(CreateView):
	model = Booking 
	fields =['booking_date', 'party_size']
	


# Create your views here.
