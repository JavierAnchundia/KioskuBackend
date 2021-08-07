from django.contrib import admin
from .models import *
# Register your models here.


# Register your models here.
myModels = [Ciudad, Provincia, Membresia, User, Bodega, CarroCompras, Categoria, Subcategoria,
            Estado, Item, MetodoPago, Producto, ImagenProducto, ImagenItem,
            Factura, EstadoCompra, CarroProducto, BodegaItem, AdminProducto, AdminItem,
            Anuncio]  # iterable list
admin.site.register(myModels)