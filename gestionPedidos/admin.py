from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono") #los campos que queremos ver en el panel de admin en clientes 
    search_fields = ("nombre", "telefono") #en el admin podremos hacer busquedas por nombre y telefono, crea un buscador


class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion",) #en el panel admin crea un filtro para poder filtrar los articulos por sección 

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha") #campos que queremos ver en el admin
    list_filter = ("fecha",) #puedes filtrar por fechas
    date_hierarchy = "fecha" #aparece el filtro en la parte superior en horizontal

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)