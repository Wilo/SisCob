from django.contrib import admin
from app.models import *
# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_filter = ('Modelo',)
    list_display = ['Cliente','Modelo','Marca','Color','Anio','Estado']

class LocalInline(admin.TabularInline):
    model = Local


class PrediosInline(admin.TabularInline):
    model = Predio

class VehiculoInline(admin.TabularInline):
    model = Vehiculo

class ClienteAdmin(admin.ModelAdmin):
    list_filter = ('Nombre',)
    inlines = [
        LocalInline,
        PrediosInline,
        VehiculoInline,
    ]
class CiudadelaAdmin(admin.ModelAdmin):
    list_filter = ('Descripcion','Usuario',)
    search_fields = ['Descripcion','Usuario']
    list_display = ('id','Descripcion', 'Usuario', 'Fecha',)

#Registrando Modelos en el Admin
admin.site.register(Aseguradora)
admin.site.register(Bombero)
admin.site.register(Ciudadela,CiudadelaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Local)
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Tipo_Cobro)
admin.site.register(Predio)
admin.site.register(Tipo_Costo_Vario)
admin.site.register(Permiso)
admin.site.register(Trans_Predio)
admin.site.register(Combustible)
admin.site.register(Cobro_Predios)
admin.site.register(Trans_Costo_Vario)