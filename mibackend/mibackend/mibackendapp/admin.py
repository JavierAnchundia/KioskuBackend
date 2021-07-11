from django.contrib import admin
from .models import *
# Register your models here.


# Register your models here.
myModels = [Ciudad, Provincia, Membresia, User, Bodega, CarroCompras, Estado, Item, MetodoPago, Producto, ImagenProducto, ImagenItem,
            Factura, EstadoCompra, CarroProducto, BodegaItem, AdminProducto, AdminItem]  # iterable list
admin.site.register(myModels)