from django.urls import path
from . import views
from .views import lista_habitaciones, crear_habitacion, editar_habitacion, eliminar_habitacion

urlpatterns = [
    path('', views.index, name='index'),
    path('habitaciones/', lista_habitaciones, name='lista_habitaciones'),
    path('habitaciones/nueva/', crear_habitacion, name='crear_habitacion'),
    path('habitaciones/<int:pk>/editar/', editar_habitacion, name='editar_habitacion'),
    path('habitaciones/<int:pk>/eliminar/', eliminar_habitacion, name='eliminar_habitacion'),
]



