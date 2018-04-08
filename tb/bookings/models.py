from django.db import models
from django.utils import timezone 
from datetime import datetime

class User(models.Model): 
	name= models.CharField(max_length=80)
	user_idcd = models.AutoField(primary_key=True)


class Booking(models.Model):
	booking_date = models.DateTimeField('Date booked')
	user_num = models.ForeignKey('User', on_delete=models.CASCADE)
	booking_ref = models.UUIDField(primary_key=True, editable= False)
	party_size = models.SmallIntegerField() 

# Create your models here.
