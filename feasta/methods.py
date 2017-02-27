from feasta.models import Session,Absent, Student, NonStudent, Meal
from django.utils.timezone import now, timedelta
def currentSession():
	session = Session.objects.filter(startdate__lte=now(), enddate__gte=now())
	if len(session) > 0:
		session = session[0]
	else:
		session = Session.objects.all()[-1]
		
	return session
	


def getSessionEndDays():
	days_left = (currentSession().enddate - now().date()).days
	return days_left
def populateNextDay(day):
	return day + timedelta(days=1)

def getNextMeal(day,meal):
	
	NEXT_MEAL={
		'BF':'L',
		'L':'D',
		'D':'BF'
	}
	NEXT_DAY = {
		'BF':day,
		'L':day,
		'D':day + timedelta(days=1)
	}
 	return [NEXT_DAY[str(meal)], NEXT_MEAL[str(meal)]]

def getUserType(user):
	Result = "NA"
	if Student.objects.filter(user=user).exists():
		Result = "STUDENT"
	elif NonStudent.objects.filter(user=user).exists():	
		Result = "NONSTUDENT"
	return Result	
def getNotEaten(user):
	cs = currentSession()
	absents = Absent.objects.filter(booked_by=user).filter(date__gte=cs.startdate).filter(date__lte=cs.enddate)
	bf = absents.filter(bf=True)
	lunch= absents.filter(lunch=True)
	dinner= absents.filter(dinner=True)
	return {'bf':bf,'lunch':lunch,'dinner':dinner}
