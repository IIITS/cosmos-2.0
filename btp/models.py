from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from btp import choices, values
import datetime

def content_file_name(instance, filename):
    return '/'.join(['evaluation/submissions', str(instance.projectgroup.project.code)+'_Report_'+str(instance.week.week.weekno)+"."+str(filename.split('.')[-1])])


class Application(models.Model):
	name = models.CharField(max_length=50)

class Batch(models.Model):
	
	background_css = models.TextField()
	admission_year = models.CharField(max_length=4)  
	graduate_year = models.CharField(max_length=4)
	btp_start_year = models.CharField(max_length=4)
	btp_end_year = models.CharField(max_length=4)
	honors_start_year = models.CharField(max_length=4)
	honors_end_year = models.CharField(max_length=4)
	def __str__(self):
		return self.admission_year+ " - "+self.graduate_year
	class Meta:
	        verbose_name_plural = "Batches"
        
class Project(models.Model):
	code = models.TextField()
	title =  models.TextField()
	description = models.TextField()
	keywords = models.TextField()
	typeOfProject= models.TextField()
	supervisors = models.TextField()
	year= models.TextField()
	summer =models.TextField()
	is_taken = models.BooleanField(default=False)
	students = models.TextField()
	def __str__(self):
		return str(self.code)+" - "+str(self.title) + "  "+ str(self.supervisors)
	def take_project(self, students):
		self.is_taken = True
		self.students = students
		return self.is_taken

	def add_students(self, students):
		self.students = self.students + ' ' + students
		return self.students
	def get_students(self):
		students = []
		st = self.students.split()
		print st
		for i in range(len(st)):
			s = st[i]
			stud = Student.objects.get(user__username=str(s))
			students.append(stud)
			print students
		return students
class ProjectMedia(models.Model):
	file_up = models.FileField(upload_to='static/files/')	
	project = models.ForeignKey(Project)

class Student(models.Model):
	user = models.OneToOneField(User)
	year = models.CharField(max_length=4, default='2016')
	def __str__(self):
		return self.user.get_full_name()
	
class Faculty(models.Model):
	class Meta:
        	verbose_name_plural = "Faculties"

	user = models.OneToOneField(User)
	area_of_interest = models.TextField(default='Not Provided')
	next_code_int = models.CharField(default='001', max_length=15) 
	code_verbose = models.CharField(default='EX', max_length=10)
	def __str__(self):
		return str(self.user.get_full_name())
	
	def fullname(self):
		return self.user.get_full_name()
	def get_all_projects(self):
		ProjectList = []
		pro = Project.objects.all()
		for p in pro:
			if (self.user.username in p.supervisors):
				ProjectList.append(p)
		self.next_code_int = values.get('beautify_digit')[str(len(ProjectList) + 1)]
		return ProjectList
	def get_btp_projects(self):
		return Project.objects.filter(typeOfProject="btp",supervisors__icontains=self.user.username).order_by('code')
	def get_honors_projects(self):	
		return Project.objects.filter(typeOfProject="honors",supervisors__icontains=self.user.username).order_by('code')
	def get_next_code(self):
		return self.code_verbose + self.next_code_int 
	
 	def aoi(self):
 		return self.area_of_interest.split(',')		
class Semester(models.Model):
	name = models.CharField(max_length=15)
	sem = models.SmallIntegerField()
	batch = models.CharField(max_length=5,choices=choices.YEAR_BATCHES)
	start = models.DateField() 
	end = models.DateField()
class BTPWeek(models.Model):
	semester = models.ForeignKey(Semester)
	weekno = models.PositiveIntegerField(default=0)
	starttime = models.DateTimeField()
	endtime = models.DateTimeField()
	def __str__(self):
		return "Week - "+str(self.weekno)
	
					

class BTPEvalPanel(models.Model):
	name = models.CharField(max_length=15)
	members = models.TextField()
	def __str__(self):
		return str(self.name)


class BTPProjectGroup(models.Model):
	project = models.ForeignKey(Project)
	students = models.TextField()
	faculty = models.TextField()
	def __str__(self):
		return self.project.code

class BTPEvalSet(models.Model):
	groupno = models.PositiveIntegerField(default=0)
	projectgroups = models.TextField()
	panel = models.ForeignKey(BTPEvalPanel)
	def __str__(self):
		return "set  - "+str(self.groupno)


class BTPSetWeek(models.Model):
	sets = models.ForeignKey(BTPEvalSet)
	week = models.ForeignKey(BTPWeek)
	evalday = models.DateField(default=timezone.now())
	starttime = models.DateField()
	endtime = models.DateField()
	submitdeadline = models.DateTimeField()
	def __str__(self):
		return "Set - "+str(self.sets.groupno) + " Week -"+str(self.week.weekno)	
class BTPSubmission(models.Model):
	week = models.ForeignKey(BTPSetWeek)
	projectgroup = models.ForeignKey(BTPProjectGroup,null=True)
	submitted_at = models.DateTimeField(auto_now = True)
	fileuploaded = models.FileField(upload_to=content_file_name)
	submitted_by = models.ForeignKey(User)
	def __str__(self):
		return str(self.week) + str(self.projectgroup) 
	def get_filename(self):
		fname=str(self.projectgroup.project.code)+'_Report_'+str(self.week.week.weekno)+"."+str(self.fileuploaded.name.split('.')[-1])
		return fname

class Resources(models.Model):
	class Meta:
        	verbose_name_plural = "Resources"

	code = models.CharField(max_length = 25) 
	fileupload = models.FileField(upload_to='/static/btp/files/')

class BTPMarks(models.Model):
	class Meta:
	        verbose_name_plural = "BTPMarks"
	semester = models.ForeignKey(Semester) 
	projectgroup = models.ForeignKey(BTPProjectGroup)
	panelmarks = models.PositiveIntegerField(default=0)
	panelstrength = models.PositiveIntegerField(default=0)
	paneltime = models.DateTimeField(auto_now=True, auto_now_add = False)
	externalmarks = models.PositiveIntegerField(default=0)
	externaltime = models.DateTimeField(auto_now=True, auto_now_add = False)
	btpcmarks = models.PositiveIntegerField(default=0)
	btpctime = models.DateTimeField(auto_now=True, auto_now_add = False)
	supervisormarks = models.PositiveIntegerField(default=0)
	supervisortime = models.DateTimeField(auto_now=True, auto_now_add = False)
	bonusmarks = models.PositiveIntegerField(default=0)
	bonusmarkstime = models.DateTimeField(auto_now=True, auto_now_add = False)
	btpweek = models.ForeignKey(BTPWeek)

	def supervisorMarksEntry(self, marks):
		self.supervisormarks = marks
		
		return True
	def panelMarksEntry(self,marks, week):
		pmarks = self.panelmarks
		pmarks = pmarks + marks
		self.panelmarks = pmarks
		self.panelstrength = self.panelstrength + 1
		
		return True
	def btpcMarksEntry(self,marks,week):
		self.btpcmarks = marks
		
		return True 	
	def bonusMarksEntry(self, marks):
            	self.bonusmarks = marks
		self.bonusmarkstime = time
		return True		
	def externalMarksEntry(self, marks):
		self.externalmarks = marks
		
		return True

	def getSuperVisorMarks(self):
		return self.supervisormarks 
	def getBTPCMarks(self):
		return self.btpcmarks
	def getExternalMarks(self):
		return self.externalmarks
	def getBonusMarks(self):
		return self.bonusmarks
	def getPanelMarks(self):
		return ( self.panelmarks * 1.0) / ( self.panelstrength * 1.0)

