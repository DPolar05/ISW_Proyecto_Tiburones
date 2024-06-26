# administracion/urls.py

from django.urls import path
from django.views.decorators.http import require_POST
from django.contrib.auth.views import LogoutView
from .views import (
    AdministracionHomeView,
    AdministracionSubirDoc,
    AdministracionTitulacion,
    AdministracionConvocatorias,
    AdministracionSeminarios,
    AdministracionInformacion,
    # titulacion
    AdministracionTitulacionConvocatorias,
    AdministracionTitulacionCalendario,
    AdministracionTitulacionRegistrar,
    # cuentas
    AdministracionAdminCuentas,
    AdministracionCreacionCuentas,
    # alumnos
    AdministracionAlumnos

)

app_name = 'administracion'  # Este es el namespace que debe coincidir con el utilizado en 'resolve_url'

urlpatterns = [
    path('home/', AdministracionHomeView.as_view(), name='home'),
    path('logout/', require_POST(LogoutView.as_view()), name='admin-logout'),

    path('informacion/', AdministracionInformacion.as_view(), name='informacion'),
    path('subir_documento/', AdministracionSubirDoc.as_view(), name='subir_documento'),
     path('titulacion/', AdministracionTitulacion.as_view(), name='titulacion'),
    path('seminarios/', AdministracionSeminarios.as_view(), name='seminarios'),
    path('convocatorias/', AdministracionConvocatorias.as_view(), name='convocatorias'),
    
    # titulacion
    path('titulacion/registrar_formas_titulacion/', AdministracionTitulacionRegistrar.as_view(), name='registrar_formas_de_titulacion'),
    path('titulacion/calendario_titulacion/', AdministracionTitulacionCalendario.as_view(), name='calendario_titulacion'),
    path('titulacion/convocatorias_titulacion/', AdministracionTitulacionConvocatorias.as_view(), name='convocatorias_titulacion'),
    
    # cuentas
    path('cuentas/administrar_cuentas/', AdministracionAdminCuentas.as_view(), name='administrar_cuentas'),
    path('cuentas/crear_cuentas/', AdministracionCreacionCuentas.as_view(), name='crear_cuentas'),

    # alumnos
    path('alumnos/', AdministracionAlumnos.as_view(), name='alumnos'),
]
