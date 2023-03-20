from . import views
from django.urls import path

urlpatterns = [
    path('', views.favourites, name="favourites_home"),
]