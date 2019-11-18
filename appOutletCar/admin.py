from django.contrib import admin

from .models import Marca, Modelo, Coche, Usuario, Lugar 
# Register your models here.

class LugarAdmin(admin.ModelAdmin):
    list_display = ('cod_ciudad', 'ciudad', 'provincia')
    search_fields = ['nombre', 'content']
  
admin.site.register(Lugar, LugarAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre_Marca', 'descripcion', 'fecha_creacion')
    search_fields = ['nombre', 'content']
  
admin.site.register(Marca, MarcaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre_Modelo', 'categoria', 'traccion', 'marca')
    search_fields = ['nombre', 'content']
  
admin.site.register(Modelo, ModeloAdmin)

class CocheAdmin(admin.ModelAdmin):
    list_display = ('n_bastidor', 'color', 'anyo', 'n_km', 'combustible', 'potencia', 'precio', 'cambio', 'consumo', 'comentario', 'modelo', 'lugar', 'fotoCoche')
    search_fields = ['bastidor', 'content']
  
admin.site.register(Coche, CocheAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('correo', 'nombre_usuario', 'apellidos', 'telefono', 'contrasenya', 'coche')
    search_fields = ['nombre', 'content']
  
admin.site.register(Usuario, UsuarioAdmin)