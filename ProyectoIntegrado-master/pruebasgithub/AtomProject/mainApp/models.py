from django.db import models

# Create your models here.
class Cliente(models.Model):
    run = models.CharField(max_length=12, null=True, blank=True)
    nombre_cliente = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre_cliente

class Estado(models.Model):
    tipo_estado = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_estado

class Marca(models.Model):
    nom_marca = models.CharField(max_length=20)
    img_marca = models.BinaryField(null=True, blank=True)  # Si usas imágenes reales, cambia por ImageField

    def __str__(self):
        return self.nom_marca

class Modelo(models.Model):
    nombre_modelo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_modelo

class OrdenDeTrabajo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Equivale a la clase auth_user
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    total_pagar = models.IntegerField()
    abono = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)
    clave = models.CharField(max_length=20, null=True, blank=True)
    observaciones = models.CharField(max_length=200)
    especificaciones = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Orden #{self.pk} - {self.cliente.nombre_cliente}"