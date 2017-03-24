from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from courses.models import Course, CourseProject
# Create your views here.
class CoursesView(ListView):
	model = Course
	template_name = "courses/courses_view.html"
	context_object_name = "course_list"

class CoursePageView(TemplateView):
	template_name = "courses/courses_page.html"
	context_object_name = "course_project_list"
	def get_context_data(self, **kwargs):
		return {
			'course_project_list': CourseProject.objects.filter(course__id=self.kwargs['id']).order_by('group_no'),
			'page_title':Course.objects.get(id=self.kwargs['id']).title
		}