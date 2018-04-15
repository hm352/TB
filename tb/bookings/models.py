from django.db import models
from django.utils import timezone 
from datetime import datetime

from django.contrib.auth.models import User



class Booking(models.Model):
	booking_date = models.DateTimeField('Date booked')
	booking_ref = models.UUIDField(primary_key=True, editable= False)
	party_size = models.SmallIntegerField() 

# Create your models here.
