from rest_framework import serializers
from afiliados.models import Afiliado

class AfiliadoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Afiliado
        fields = ( 'nombre', 'apellido', 'fecha_afiliacion')