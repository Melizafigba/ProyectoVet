from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.bienvenido),
    path('lista_post',views.lista_post),
    path('almacenar', views.almacenar),
    path('editar',views.editar),
   
    
]
