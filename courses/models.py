from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	identifier = models.CharField(max_length=50, unique=True)
	title = models.CharField(max_length=220)

	def __str__(self):
		return self.title

class CourseProject(models.Model):
	# Project Type Legend
	# 0 - Individual
	# 1 - Group
	group_no = models.IntegerField(default=0)
	project_type = models.IntegerField(default=1)
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=220)
	description = models.TextField(default='Not Description Available')
	link = models.URLField()

	def __str__(self):
		return self.title
	