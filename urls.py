from django.conf.urls import patterns, include, url
from test_dm.dynamic_models import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^$', views.index,{'app':'dynamic_models'}),
    (r'^addrow/$', views.index,{'app':'dynamic_models'}),
    #(r'^edit/$', views.edit,{'app':'dynamic_models'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
