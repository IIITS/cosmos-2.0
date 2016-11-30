from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from btp import views as btp_views

urlpatterns = [
	url(r'^$', login_required(btp_views.IndexView.as_view()), name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^btp/', include('btp.urls', namespace='btp')),
    url(r'^btp/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^issues-and-suggestions/', include('gp.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
handler404 = 'btp.views.page_not_found'

