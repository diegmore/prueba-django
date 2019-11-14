from django.conf.urls import url
from django.urls import path,include
from .views import index_a,SolicitudList,SolicitudCreate, SolicitudUpdate, SolicitudDelete
app_name = 'adopciones'
urlpatterns = [
	url(r'^$',index_a),
	path('solicitud/listar',SolicitudList.as_view(),name='solicitud_listar'),
	path('solicitud/nueva',SolicitudCreate.as_view(),name='solicitud_crear'),
	path('solicitud/editar/<int:pk>',SolicitudUpdate.as_view(),name='solicitud_editar'),
	path('solicitud/eliminar/<int:pk>',SolicitudDelete.as_view(),name='solicitud_eliminar'),
]
