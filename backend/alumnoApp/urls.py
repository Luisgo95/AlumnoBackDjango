from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from alumnoApp.viewsets import AlumnoViewset

router = DefaultRouter()
router.register(r'alumno', AlumnoViewset , basename='alumno')

urlpatterns = [
    path('alumnoApp/', include(router.urls)),
    # url(r"^alumnoApp/token", obtain_auth_token, name="alumnoApp-token"),
    # path('alumnoApp-auth/', include('rest_framework.urls')),
]
