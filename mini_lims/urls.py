from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mini_lims.views.home', name='home'),
    url(r'^orga_run/', include('orga_run.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
