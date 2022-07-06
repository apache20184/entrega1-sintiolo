from django.urls import path
from .views import creacion_tablas, inicio, listadovista, nosotros

urlpatterns = [
  path('', inicio, name='inicio' ),
  path('creacion_tablas/', creacion_tablas , name='creacion_tablas' ),
  path('formulario/', listadovista , name='listado'),
  path('paginanosotros/', nosotros , name='nosotros')
  ]