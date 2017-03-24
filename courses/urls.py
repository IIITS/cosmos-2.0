from django.conf.urls import url
from courses import views
urlpatterns = [
	# Individual Course Page
	url(r'^course-page/c/(?P<id>[0-9]+)/$', views.CoursePageView.as_view()),
	# Lists all courses
	url(r'^$', views.CoursesView.as_view())
	]