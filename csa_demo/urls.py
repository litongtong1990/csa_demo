from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.stream_apfloor, name='stream_apfloor'),      
    url(r'^stream/$', views.stream, name='stream'),
    url(r'^stream_ds/$', views.stream_ds, name='stream_ds'),        

    url(r'^stream_apfloor/$', views.stream_apfloor, name='stream_apfloor'),   
    url(r'^api_apfloor/$', views.api_apfloor, name='api_apfloor'),  
    url(r'^api_apfloor_min/$', views.api_apfloor_min, name='api_apfloor_min'),            
]
