from django.shortcuts import render
from .models import User, Booking
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 

from .forms import booking_form


def homepage(request):
	return render(request, 'bookings/index.html')

def booking(request):
	
	if request.method =='POST':
		#creating form instnce and populate it with data
		form = booking_form(request.POST)

		if form.is_valid():

			Booking = f.save()

			return HttpResponse('Thank you for your booking')

		else: 
			return HttpResponse("sorry we weren't able to process those booking details")

	
	else: 
		form = booking_form()

		return render(request, 'booking/booking_form.html', {'form':form})


def booking_page(request):
	user = User(name='Henry Maher')
	user.save()
	return HttpResponse(User.objects.get(pk=1).name)


# Create your views here.
