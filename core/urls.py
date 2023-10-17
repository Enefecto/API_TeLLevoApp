from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('viajes/', views.viajes_list, name='viajes_list'),
    path('viajes/<int:pk>/', views.viaje_detail, name='viaje_detail'),
]
