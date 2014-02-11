from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siscobros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('siscobros.apps.main.urls')),
    url(r'^$', 'django.contrib.auth.views.login',{ 'template_name': 'main/login.html'}, name="login"),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name="logout"),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
