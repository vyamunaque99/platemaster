from django.db import models

class DataEntryVehiculo(models.Model):
    """Modelo para almacenar datos de vehículos extraídos de imágenes SUNARP."""

    num_placa = models.CharField(max_length=1024, unique=True)
    num_serie = models.CharField(max_length=1024, blank=True)
    num_vin = models.CharField(max_length=1024, blank=True)
    num_motor = models.CharField(max_length=1024, blank=True)
    color = models.CharField(max_length=1024, blank=True)
    marca = models.CharField(max_length=1024, blank=True)
    modelo = models.CharField(max_length=1024, blank=True)
    placa_vigente = models.CharField(max_length=1024, blank=True)
    placa_anterior = models.CharField(max_length=1024, blank=True)
    estado = models.CharField(max_length=1024, blank=True)
    anotaciones = models.TextField(blank=True)
    sede = models.CharField(max_length=1024, blank=True)
    anio_modelo = models.CharField(max_length=1024, blank=True)
    propietarios = models.CharField(max_length=1024, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ["-created_at"]
        db_table = 'de_vehiculo'

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.num_placa}"
