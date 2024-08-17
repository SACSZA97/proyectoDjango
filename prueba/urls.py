"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/',views_registros.contacto, name="Contacto"),
    path('formulario/',views.formulario, name="Formulario"),
    path('ejemplo/',views.ejemplo, name="Ejemplo"),
    path('',views_registros.registros, name="Principal"),
    path('registrar/',views_registros.registrar, name="Registrar"),
    path('consultarComentario/',views_registros.comentario, name="ConsultarComentarios"),
    path('consultarContacto/',views_registros.comentarioContacto, name="ConsultarContacto"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto,name='Editar'),
    path('consultas1',views_registros.consultar1,name="Consultas"),
    path('consultas2',views_registros.consultar2,name="Consultas2"),
    path('consultas3',views_registros.consultar3,name="Consultas3"),
    path('consultas4',views_registros.consultar4,name="Consulta4"),
    path('consultas5',views_registros.consultar5,name="Consulta5"),
    path('consultas6',views_registros.consultar6,name="Consulta6"),
    path('consultas7',views_registros.consultar7,name="Consulta7"),
    path('consultasSQL',views_registros.consultasSQL,name="sql"),
]

if settings.DEBUG:
     from django.conf.urls.static import static
     urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
