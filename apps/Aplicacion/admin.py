from django.contrib import admin
from .models import Ropa,Cliente,Factura,Orden,OrdenDetalle,TipoRopa

# Register your models here.

admin.site.register(TipoRopa)
admin.site.register(Ropa)
admin.site.register(Cliente)


class OrdenDetalleInline(admin.TabularInline):
    '''Tabular Inline View for OrderDetail'''

    model = OrdenDetalle
    extra =0


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    '''Admin View for Invoice'''

    list_display = ('numero_factura','cliente', 'orden','fecha','pago')
    ordering = ('numero_factura','fecha',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ['id', 'fecha', 'total' ]
    inlines = [OrdenDetalleInline]