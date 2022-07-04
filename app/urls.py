from django.urls import path
from app.views import creacion_tablas

urlpatterns = [
    path('', creacion_tablas),
  ]