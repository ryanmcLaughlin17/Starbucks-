from . import views
from django.urls import path

urlpatterns = [
    path('', views.menu, name="menu_home"),
]