from django.db import models
from django.utils import timezone

# Create your models here.
class Afiliado(models.Model):
    nombre=models.CharField(max_length=50, blank=True, null=True)
    apellido=models.CharField(max_length=50, blank=True, null=True)
    fecha_afiliacion=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-fecha_afiliacion',) # Orden por defecto de los Afiliados es por fecha de afiliacion desc
