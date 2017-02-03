from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader	
from .models import Room,time,books
from django.shortcuts import render_to_response, render
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.db.models import When

@csrf_protect
def login(request):
	c = {}
	return render(request,'login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/polls')
	else:
		return HttpResponseRedirect('/polls/accounts/invalid')
def index(request):
	all_rooms = Room.objects.all()
	template = loader.get_template('polls/index.html')
	full_name = request.user.username
	context = {
		'all_rooms' : all_rooms,
		'full_name' : full_name, 
	}
	if request.user.is_authenticated:
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/polls/accounts/login')	
def invalid_login(request):
	return render_to_response('invalid.html')
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/polls/accounts/login')	
def details(request, room_id):
	all_rooms = Room.objects.all()
	template = loader.get_template('polls/detail.html')
	specific_room = Room.objects.get(pk = room_id)

	context = {
		'all_rooms' : all_rooms,
		'specific_room' : specific_room,
	}
	if request.user.is_authenticated:
		return HttpResponse(template.render(context,request))
	else:
		return HttpResponseRedirect('/polls/accounts/login')
def book(request, room_id, room_no):
	template = loader.get_template('polls/book.html')
	room = Room.objects.get(pk=room_id)
	context = {
		'room' : room,
	}
	if request.user.is_authenticated:
		return HttpResponse(template.render(context,request))
	else:
		return HttpResponseRedirect('/polls/accounts/login')
def confirm(request, room_id, room_no, date_of_booking):
	#ate_of_booking = request.args[0]
	time_slots = time.objects.all()
	template = loader.get_template('polls/confirm.html')
	room = Room.objects.get(pk= room_id)
	list_of_time = []
	try:
		booked_room = list(books.objects.filter(room_no=room_no,date_of_booking=date_of_booking).values())		
		# for i in booked_room:
		# 	list_of_time['i'] = booked_room[i].time
		for i in range(len(booked_room)):
			list_of_time.insert(i, booked_room[i]['time'])
		print list_of_time
	except books.DoesNotExist:
		booked_room = None
		list_of_time = []
	#booked_room = books.objects.raw('SELECT time FROM books')
	context = {
		'time_slots':time_slots,
		'room' : room,
		'date_of_booking' : date_of_booking,
		'booked_room': list_of_time	,
	}
	if request.user.is_authenticated:
		return HttpResponse(template.render(context,request))
	else:
		return HttpResponseRedirect('/polls/accounts/login')
def booking(request,room_no,date_of_booking,time_id,room_id):
	if request.user.is_authenticated:
		email_id = request.user.email 
		template = loader.get_template('polls/booking.html')
		book_entry = books(room_no = room_no, email=email_id, time= time_id, date_of_booking=date_of_booking)
		book_entry.save()
		if book_entry.save() :
			send_mail('Room Booked','Room booked by'+request.user.first_name, email_id, ['akash.d14@iiits.in'])
			context = {
				'email_id':email_id,
			}
			return HttpResponseRedirect('/polls/'+room_id+'/'+room_no+'/'+date_of_booking)
