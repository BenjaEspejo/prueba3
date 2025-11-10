from django.contrib import admin
from .models import Cliente, Estado, Marca, Modelo, OrdenDeTrabajo

# Register your models here.
from django.contrib import admin
from .models import Cliente, Estado, Marca, Modelo, OrdenDeTrabajo

admin.site.register(Cliente)
admin.site.register(Estado)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(OrdenDeTrabajo)
