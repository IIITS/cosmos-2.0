from __future__ import unicode_literals
import datetime	 
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from calendar import HTMLCalendar
from django import template
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

register = template.Library()

# Create your models here.

class Room(models.Model):
	room_no = models.IntegerField(default = 0)
	no_of_seats = models.IntegerField(default = 0)
	air_conditioned = models.BooleanField(default = False)
	duration = models.IntegerField(default = 1)
	room_name = models.CharField(max_length=50, default = '')
	def __str__(self):
		return self.room_name	


class time(models.Model):
	start_time = models.CharField(blank = True,null=True, max_length=50)
	finish_time = models.CharField(blank = True	, null = True, max_length=50)
	def __str__(self):
		return "{}-{}".format(self.start_time, self.finish_time) 

class books(models.Model):
	date_of_booking = models.DateField(null=True)
	time  = models.CharField(null=False, max_length=50)
	room_no = models.IntegerField(null=False)
	email = models.CharField(max_length=100,null=False, default='')
	def __str__(self):
		return self.time

