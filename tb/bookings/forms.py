from django import forms 
from .models import Booking

class booking_form(forms.ModelForm):
	"""docstring for booking_form"""
	class Meta:
		model = Booking
		fields = ['booking_date','party_size']
