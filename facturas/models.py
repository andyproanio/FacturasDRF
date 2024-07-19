from django.db import models

# Create your models here.
class Inventario(models.Model):
    serie_comprobante = models.TextField()
    ruc_emisor = models.TextField()
    razon_social_emisor = models.TextField()
    fecha_emision = models.DateField()
    identificacion_receptor = models.TextField()
    subtotal_15 = models.FloatField(null=True)
    subtotal_0 = models.FloatField(null=True)
    iva = models.FloatField(null=True)
    importe_total = models.FloatField()