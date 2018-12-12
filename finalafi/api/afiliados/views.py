from django.shortcuts import render
from rest_framework import viewsets
from afiliados.serializers import AfiliadoSerializer
from afiliados.models import Afiliado

# Create your views here.
class AfiliadoViewSet(viewsets.ModelViewSet):
    queryset = Afiliado.objects.all()
    serializer_class = AfiliadoSerializer
