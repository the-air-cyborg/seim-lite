from django.urls import path
from . import views

urlpatterns = [
    path('', views.alert_dashboard, name='alert_dashboard'),
]
