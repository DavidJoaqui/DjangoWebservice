from django.conf.urls import url

from Apps.aplicacion.views import documentacion,formulario,contacto,listar,editarpersona,eliminarRegistro

urlpatterns=[
	url(r'crear/$', formulario, name='crear'),
	url(r'listapersonas/$', listar, name='listar'),
	url(r'editar/(?P<id_documento>\d+)/$', editarpersona, name='editar'),
	url(r'eliminar/(?P<id_documento>\d+)/$', eliminarRegistro, name='eliminar'),
	url(r'documentacion/$',documentacion,name='documentacion'),
	url(r'contacto/$',contacto, name="contacto"),
]