from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'starter.views.home', name='home'),
    #url(r'^your_app/', include(your_app.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

# serve local uploaded files with runserver (but not on production of course!)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )

# fallback for serving favicon.ico
urlpatterns += patterns('',
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico'))
)

# an endpoint for robots.txt
urlpatterns += patterns('',
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow:", mimetype="text/plain")),
)
