from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('contacto/',views.contacto,name='contacto'),
    path('recibir/',views.recibir),
    path('clientes/',views.clientes),
    path('reclamov2',views.reclamo2),
    path('cliente2',views.clientes2),
    path('crearusuario',views.crearUsuario),
    path('loginu',views.loginu),
    path('grupos',views.grupito)
]
