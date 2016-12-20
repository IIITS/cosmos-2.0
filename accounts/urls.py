from django.conf.urls import url
from accounts import views 
from btp.views import IndexView
from django.conf import settings
from django.contrib.auth.views import password_reset, logout
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^login/$', views.LoginView.as_view(),name='loginpage'),
	url(r'^secure/changepassword/$', login_required(views.password_change),{'post_change_redirect' : '/password-changed/','password_change_form':PasswordChangeForm}),
	url(r'^password-changed/$', login_required(IndexView.as_view()), name='password_change_done' ),
	url(r'^signout/$', views.logout_view,name='logoutpage'),
]
if settings.SERVE_MEDIA:
    urlpatterns += (
        url(r'media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
        url(r'static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, }),
)
