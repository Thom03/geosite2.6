from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from geonode.contrib.geosites.urls import urlpatterns, handler403

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
 ) + urlpatterns
