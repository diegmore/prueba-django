from django.urls import path,include
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(),name='registrar'),
]
