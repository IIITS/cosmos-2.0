from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [ 
	url(r'^accounts/login/$', views.login, name='login'),
	url(r'^accounts/logout/$', views.logout, name='logout'),
	url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
	url(r'^accounts/invalid/$', views.invalid_login, name='invalid'),
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name ='index'),
	url(r'^(?P<room_id>[0-9]+)/$', views.details, name = 'detail'),
	url(r'^(?P<room_id>[0-9]+)/(?P<room_no>[0-9]+)/$',views.book, name = 'book'),
	url(r'^(?P<room_id>[0-9]+)/(?P<room_no>[0-9]+)/(?P<date_of_booking>(\d{4})[/.-](\d{2})[/.-](\d{2}))/$',views.confirm, name = 'confirm'),
	url(r'^(?P<room_id>[0-9]+)/(?P<room_no>[0-9]+)/(?P<date_of_booking>(\d{4})[/.-](\d{2})[/.-](\d{2}))/(?P<time_id>(\d\d+)[:](\d{2}))/$',views.booking, name = 'booking'),
]
