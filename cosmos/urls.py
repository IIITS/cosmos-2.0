from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from btp import views as btp_views
from accounts import urls as accounts_urls
from posts import views as posts_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as static_serve
import settings
urlpatterns = [
	url(r'^$', login_required(btp_views.IndexView.as_view()), name='homepage'),
	url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^btp/', include('btp.urls', namespace='btp')),
    
    url(r'^issues-and-suggestions/', include('gp.urls')),
<<<<<<< HEAD

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
=======
    url(r'^polls/', include('polls.urls')),
    url(r'^roombookings/', include('polls.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
>>>>>>> 8c1491d18f4e73764cf530977a890450c1ae945f

	url(r'^feasta/', include('feasta.urls')),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^posts/', include("posts.urls", namespace='posts')),


]
handler404 = 'btp.views.page_not_found'

# During Development Phase
if settings.DEBUG ==True:
	 urlpatterns += staticfiles_urlpatterns()

	 print staticfiles_urlpatterns()
<<<<<<< HEAD

if settings.SERVE_MEDIA:
    urlpatterns += (
        url(r'media/(?P<path>.*)$', static_serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
        url(r'static/(?P<path>.*)$', static_serve,
            {'document_root': settings.STATIC_ROOT, }),
)

=======
>>>>>>> 64efa264553a2c0079ca31ea52191b99bd224ced
