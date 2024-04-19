from django.urls import path
from . import views
#* llego con esta base http://127.0.0.1:8000/productos/
app_name = 'producto' # asegurarme que exista el namespace 
urlpatterns = [
    path('',views.index, name='index'), #* llego con esta base http://127.0.0.1:8000/productos/
    path('formulario/', views.formulario, name='formulario'), #* llego con esta base http://127.0.0.1:8000/productos/formulario/
]
