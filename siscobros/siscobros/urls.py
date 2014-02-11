from django.conf.urls import patterns, include, url
import settings
from apps.main.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siscobros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index_view, name='index_view'),
    url(r'^enviar-ajax/$', enviar_ajax, name='enviar_ajax'),
    
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name="logout"),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
