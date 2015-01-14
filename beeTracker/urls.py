from django.conf.urls import patterns, include, url
from tracker.models import *
from django.contrib import admin
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trackBee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # json 
    url(r'^devices/$', 'tracker.views.devices', name='get the devices'),
    url(r'^last_location/(\d+)/$', 'tracker.views.lastLocation', name='get the last location'),
    url(r'^login/$', 'tracker.views.login', name='login'),

    # visor
    url(r'^visor/$', 'tracker.views.visor', name='visor'),

    # login
    url(r'^login/$', 'tracker.views.login', name='login'),
    
    # logout
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),

    # home
    url(r'^$', 'tracker.views.home', name='home'),
    url(r'^home/$', 'tracker.views.home', name='home'),

    # movil app POST
    url(r'^new_device/$', 'tracker.views.newDevice', name='add a new device'),
    url(r'^new_position/$', 'tracker.views.newPosition', name='add a new position'),
    url(r'^new_checkPoint/$', 'tracker.views.newCheckPoint', name='add a new checkpoint'),

    # media files
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
