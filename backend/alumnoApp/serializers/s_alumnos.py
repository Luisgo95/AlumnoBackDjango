from rest_framework import serializers
from alumnoApp.models.m_alumnos import Alumno


class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'
