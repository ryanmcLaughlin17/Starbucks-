from . import views
from django.urls import path

urlpatterns = [
    path('', views.partner, name="partner_home"),
    path('management/', views.management, name="management_home"),
    path('baristas/', views.baristas, name="baristas_home"),
    path('potq/', views.potq, name="potq_home"),
    path('coffee_master/', views.coffee_master, name="coffee_master_home"),
]
