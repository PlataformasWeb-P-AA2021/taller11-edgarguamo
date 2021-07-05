from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Crear  entidades 
    path('crear/edificio', views.crear_edificio, name='crear_edificio'),
    path('crear/departamento', views.crear_departamento, name='crear_departamento'),
    # Modificar entidades
    path('editar/edificio/<int:id>', views.editar_edificio, name='editar_edificio'),
    path('editar/departamento/<int:id>', views.editar_departamento, name='editar_departamento'),
    # Eliminar entidades
    path('eliminar/edificio/<int:id>', views.eliminar_edificio, name='eliminar_edificio'),
    path('eliminar/departamento/<int:id>', views.eliminar_departamento, name='eliminar_departamento'),    
]