from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.stream, name='stream'),   
    url(r'^stream/$', views.stream, name='stream'),  
    url(r'^api/$', views.api, name='api'),        
]
