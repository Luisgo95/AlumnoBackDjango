import json
from django.core.files import File
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, viewsets
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from alumnoApp.models import Alumno
from alumnoApp.serializers import AlumnosSerializer
from datetime import datetime, timedelta
import datetime
import calendar

class AlumnoViewset(viewsets.ModelViewSet):
    # queryset = Alumno.objects.filter(nombre)
    queryset = Alumno.objects.all()
    filter_backends = ( filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("nombre", )
    search_fields = ("nombre",)
    ordering_fields = ("nombre", )

    def get_serializer_class(self):
        """Define serializer for API"""
        if self.action == 'list' or self.action == 'retrieve':
            return AlumnosSerializer
        else:
            return AlumnosSerializer


    # def agregarDias(i):
    switcher={
            0:4,
            1:3,
            2:2,
            3:1,
            4:0,
            5:-1,
            6:5
            }

    def create(self, request, *args, **kwargs):

        data = request.data
        carnet = data.get('carnet')
        generoPoesia = data.get('generoPoesia')
        ultimodigitoCarnet = int(carnet[-1])
        fecha = datetime.datetime.now()
        if generoPoesia=='dramatico' and ultimodigitoCarnet==1:
            print("Saludos Luis Gomez 1")
            # para realizar pruebas con fechas especificas y ver si funciona
            # S='2021/06/17'
            # fecha = datetime.datetime.strptime(S,"%Y/%m/%d")
            # Evaluamos si la fecha no cae en una posicion 5 o 6 del calendario
            # ya que la posicion 5 y 6 corresponde a la posicion de fin de semana Sabado y domingo
            if (fecha.weekday() == 5 or fecha.weekday() == 6):
                if (fecha.weekday()==5):
                    fechaNueva = fecha+timedelta(days=2)
                    fechaExposicion = fechaNueva+timedelta(days=4)
                elif (fecha.weekday() ==6):
                    fechaNueva = fecha+timedelta(days=1)
                    fechaExposicion = fechaNueva+timedelta(days=4)
                else:
                    fechaExposicion = fecha
            else:
                fechaExposicion = fecha
                dias=1
                # nuestro while aumenta 5 días a la fecha no contando los dias sabados ni domingos si queremos
                # agregar 6 dias sin contar sabados ni domingos solo modificamos la condicion del while a 6 en adelante...
                while dias <= 5:
                    print(fechaExposicion.weekday())
                    if fechaExposicion.weekday() == 5 or fechaExposicion.weekday() == 6:
                        fechaExposicion = fechaExposicion+timedelta(days=1)
                    else:
                        fechaExposicion = fechaExposicion+timedelta(days=1)
                        dias+=1
        elif ultimodigitoCarnet==3 and generoPoesia =='epica':
            # if (fecha.weekday()==5):
            #     fechaNueva = fecha+timedelta(days=2)
            #     fechaExposicion = fechaNueva+timedelta(days=4)
            # elif (fecha.weekday() ==6):
            #     fechaNueva = fecha+timedelta(days=1)
            #     fechaExposicion = fechaNueva+timedelta(days=4)
            # else:
            #     fechaExposicion = fecha
            mes=fecha.month
            anio=fecha.year
            # print("Mes es ",)
            # print("año es ",)
            monthRange = calendar.monthrange(anio,mes)
            diasDelMes = monthRange[1]
            # Para probar manualmente tenemos que setear los dias y
            # setear un mes que conincida con los dias ingresados
            # para probar fecha manuales decomenta lo siguiente
            # diasDelMes = 31
            S='2021/'+str(mes)+'/'+str(diasDelMes)
            # para probar fecha manuales decomenta lo siguiente 
            # S='2021/'+'8'+'/'+str(diasDelMes)
            fechaObtenidos = datetime.datetime.strptime(S,"%Y/%m/%d")
            # diasObtenidos = int(diasDelMes)
            if (fechaObtenidos.weekday()==5):
                fechaExposicion = fechaObtenidos-timedelta(days=1)
                    # fechaExposicion = fechaNueva+timedelta(days=4)
            elif (fechaObtenidos.weekday() ==6):
                fechaExposicion = fechaObtenidos+timedelta(days=2)
                # fechaExposicion = fechaNueva+timedelta(days=4)
            else:
                fechaExposicion = fechaObtenidos
            # print ("Dia del  6 ",fecha.days(6))
            print("Saludos es 3", ultimodigitoCarnet)
        else:
            # para realizar pruebas con fechas especificas y ver si funciona
            # S='2021/06/20'
            # fecha = datetime.datetime.strptime(S,"%Y/%m/%d")
            diasAdd =self.switcher.get(fecha.weekday())
            fechaExposicion = fecha+timedelta(days=diasAdd)
        datos=Alumno.objects.create(
            carnet= data.get('carnet'),
            nombre= data.get('nombre'),
            apellidos=data.get('apellidos'),
            direccion=data.get('direccion'),
            genero=data.get('genero'),
            telefono=data.get('telefono'),
            fechaNacimiento=data.get('fechaNacimiento'),
            carrera=data.get('carrera'),
            generoPoesia=data.get('generoPoesia'),
            fechaInscripcion=datetime.datetime.now(),
            fechaExposicion=fechaExposicion
        )
        datosCompleto = AlumnosSerializer(datos)

        return Response(datosCompleto.data, status=status.HTTP_201_CREATED)

        # return Response({
        #     "Exposicion": "fechaExposicion", 
        # })   
        #     )