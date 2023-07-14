from django.contrib import admin
from .models import Vehiculo

# Register your models here.
# admin.site.register(Vehiculo)


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial_carroceria',
                    'serial_motor', 'categoria', 'precio')
