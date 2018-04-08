from django.test import TestCase, LiveServerTestCase
from .models import * 
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BookingViewsTests(LiveServerTestCase):
	def setup:(self):
		self.selenium = webdriver.ChromeDriver()
		super(BookingViewsTests, self).setup()

	def teardown(self):
		self.selenium.quit()
		super(BookingViewsTests, self).teardown

	def test_booking_signup(self):
		selenium = self.selenium
		selenium.get('http://127.0.0.1:8000/')
		assert False
# Create your tests here.
