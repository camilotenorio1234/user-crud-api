from django.db import models

class Usuario(models.Model):
    tipo_documento = models.CharField(max_length=50)
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
