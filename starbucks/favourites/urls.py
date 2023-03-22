from . import views
from django.urls import path
from django.urls.conf import include  
from django.conf import settings  


urlpatterns = [
    path('', views.favourites, name="favourites_home"),
]

