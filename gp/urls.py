from django.conf.urls import url
from gp.views import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_change

urlpatterns = [
			url(r'^$', homeRedirect),
			url(r'^complaint/post/$',PostComplaint.as_view(),name = 'postcomplaint'),
			url(r'^complaints/view/$',ViewComplaintByDomain.as_view(),name= 'complaints'),
			url(r'^upvote/complaint/',Upvotes,name = 'upvote'),
			url(r'^mycomplaints/$',viewMyComplaints.as_view(),name='mycomplaints'),
			url(r'^submit/suggestion/$', submitSuggestion, name='submitsuggestion'),
			url(r'^get/suggestion/$', getSuggestions, name='getsuggestion'),
			]
