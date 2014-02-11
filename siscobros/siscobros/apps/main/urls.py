from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('siscobros.apps.main.views',
                       url(r'^index/', 'main_view', name="vista_principal"),
                       url(r'^demo/','Demo_view',name="demo"),
                       url(r'^auto/','autocomplete',name='auto'),
                       url(r'^auto/getvalue','get_value',name='prueba'),
                       )




