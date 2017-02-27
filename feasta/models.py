from __future__ import unicode_literals
from django.db.models import *
from django.contrib.auth.models import User
from django.utils.timezone import now
from feasta.config import model_choices

class Application(Model):
	name = CharField(max_length=50) 
	title = TextField(default='Feasta | Mess @ IIITS')

class UserEntity(Model):
	user = OneToOneField(User)
	permissions = TextField(default='NA')
	is_admin = BooleanField(default=False)

class Session(Model):
	name = CharField(max_length=50)
	year = CharField( max_length=4, choices=model_choices['YEAR_CHOICES'], default=now().year)
	startdate = DateField(auto_now=False, auto_now_add=False) 
	enddate = DateField(auto_now=False, auto_now_add=False)
	class Meta:
		unique_together = (("year","name"), ("startdate","enddate"))
class Meal(Model):
	name = CharField(max_length=50, choices=model_choices['MEAL'])
	starttime = TimeField(auto_now=False, auto_now_add=False)
	endtime = TimeField(auto_now=False, auto_now_add=False)
	def __str__(self):
		return str(self.name)
	def getname(self):
		parse = {'BF':'Break Fast', 'L':'Lunch', 'D':'Dinner'}
		return parse[self.name]
	def getCode(self):
		return self.name	
class Mess(Model):
	name = CharField(max_length=50)
	vendors = TextField(default='NA')
	description = TextField(default='NA')
class Menu(Model):
	mess=ForeignKey(Mess,on_delete=CASCADE)
	meal = ForeignKey(Meal,on_delete=CASCADE)
	day = CharField(max_length=20, choices=model_choices['WEEK_DAY'])
	items = TextField(default='NA')	
class Vendor(Model):
	name = CharField(max_length=50)
	description = TextField(default='NA')
class Student(UserEntity,Model):
	rollno = CharField(max_length=20)
	batch = CharField(max_length=20, choices=model_choices['BATCH'])
	branch = CharField(max_length=20, choices=model_choices['BRANCH'])
	default_mess = ForeignKey(Mess)
class NonStudent(UserEntity,Model):		
	nstype = CharField(max_length=20, choices=model_choices['NON_STUDENT_TYPE'])
	


class Absent(Model):
	booked_by = ForeignKey(User,db_index=True)
	booked_time = DateTimeField(auto_now_add=True)
	bf= BooleanField(default=False)
	lunch=BooleanField(default=False)
	dinner=BooleanField(default=False)
	date = DateField(db_index=True)
	class Meta:
		unique_together = (("booked_by","date"))
		index_together = (("booked_by","date"))

class GuestAdd(Model):
	booked_by=ForeignKey(User)
	booked_time=DateTimeField(auto_now_add=True)
	guest_name = CharField(max_length=100)
	meal = ForeignKey(Meal)
	day = DateField(editable=True)
class SummerRegistration(Model):
	booked_by=ForeignKey(User)
	booked_time=DateTimeField(auto_now_add=True)
	start_date = DateField(editable=True)
	end_date = DateField(editable=True)

class SummerRegistrationPickDates(Model):
	booked_by=ForeignKey(User)
	booked_time=DateTimeField(auto_now_add=True)
	dates = TextField()
