from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from btp import views as btp_views
from accounts import urls as accounts_urls
from posts import views as posts_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
urlpatterns = [
	url(r'^$', login_required(btp_views.IndexView.as_view()), name='homepage'),
	url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^btp/', include('btp.urls', namespace='btp')),
    url(r'^/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^issues-and-suggestions/', include('gp.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^roombookings/', include('polls.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	url(r'^feasta/', include('feasta.urls')),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^posts/', include("posts.urls", namespace='posts')),

	url(r'^exam_schedule',posts_views.getSchedule.as_view())#for showing exam_schedule

]
handler404 = 'btp.views.page_not_found'

# During Development Phase
if settings.DEBUG ==True:
	 urlpatterns += staticfiles_urlpatterns()

	 print staticfiles_urlpatterns()
