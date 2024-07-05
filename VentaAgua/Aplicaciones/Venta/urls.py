from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarPedido/', views.registrarPedido),
    path('edicionPedido/<codigo>', views.edicionPedido),
    path('editarPedido/', views.editarPedido),
    path('eliminarPedido/<codigo>', views.eliminarPedido)
]
