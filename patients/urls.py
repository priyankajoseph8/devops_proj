from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('<int:pk>/', views.patient_detail, name='patient_detail'),
    path('new/', views.patient_create, name='patient_create')]