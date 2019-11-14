
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from .views import index,mascota_view,mascota_list,mascota_edit,mascota_delete, MascotaList, MascotaCreate,MascotaUpdate,\
MascotaDelete
app_name = 'mascota'
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^nuevo$', MascotaCreate.as_view(),name='crear'),
    url(r'^listar$', MascotaList.as_view(),name='lista'),
    path('editar/<int:pk>/' ,MascotaUpdate.as_view(), name='m_editar'),
    path('eliminar/<int:pk>/' ,MascotaDelete.as_view(), name='m_eliminar'),    


]
