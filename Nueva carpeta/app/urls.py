from django.urls import path
from . import views
from .views import insertar_o_actualizar

urlpatterns=[
    path('',views.index, name='index'),
    path('list_productos/',views.list_productos, name='list_productos'),
    path('insertar_o_actualizar/', insertar_o_actualizar, name='insertar_o_actualizar')
]
