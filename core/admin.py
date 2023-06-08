from django.contrib import admin
from .models import *

# Register your models here.

# PARA QUE EN EL ADMIN SE VISUALICE COMO TABLA
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','tipo','descripcion','vencimiento','imagen','vigente']
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['tipo']
    list_editable = ['precio','stock','tipo','descripcion','vencimiento','imagen','vigente']


admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)