from rest_framework import serializers
from .models import *

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class MembresiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membresia
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'password',
            'staff',
            'rol',
            'is_active',
            'saldo',
            'address',
            'provincia',
            'ciudad',
            'cedula',
            'celular',
            'membresia',
            'fechaSuscripcion'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.email = validated_data.get('email')
        user.set_password(password)
        user.save()
        return user

class UserFullSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer(required=False)
    provincia = ProvinciaSerializer(required=False)
    membresia = MembresiaSerializer(required=False)
    class Meta:
            model = User
            fields = ('id', 'name', 'email', 'address', 'is_active', 'saldo',
            'ciudad', 'provincia', 'membresia', 'cedula', 'celular', 'rol', 'fechaSuscripcion')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

        #fields = ('id', 'nombre')


class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = ('id', 'direccion', 'ciudad', 'is_active')

class BodegaCiudadSerializer(serializers.ModelSerializer):
    ciudad_name = serializers.CharField(source='ciudad.nombre')

    class Meta:
        model = Bodega
        fields = ('id', 'nombre', 'direccion', 'is_active', 'ciudad', 'ciudad_name')

class CarroComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarroCompras
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemEstadoSerializer(serializers.ModelSerializer):
    estado_name = serializers.CharField(source='estado.estado')
    estado_date_updated = serializers.CharField(source='estado.date_updated')

    class Meta:
        model = Item
        fields = ('id', 'titulo', 'descripcion', 'cantidad', 'entrega', 'creditos', 'thumbnail',
                  'estado', 'propietario', 'estado_name','estado_date_updated')

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = '__all__'

class ImagenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenItem
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class EstadoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCompra
        fields = '__all__'

class CarroProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarroProducto
        fields = '__all__'

class BodegaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaItem
        fields = '__all__'

#class BodegaProductoSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = BodegaProducto
#        fields = '__all__'

#class ProductoAndBodegaProductoSerializer(serializers.ModelSerializer):

#    estado = serializers.CharField(source='producto.estado')
#    item = serializers.CharField(source='producto.item')
#    subcategoria = serializers.CharField(source='producto.subcategoria')
#    categoria = serializers.CharField(source='producto.categoria')
#    peso = serializers.CharField(source='producto.peso')
#    precio = serializers.CharField(source='producto.precio')
#    descripcion = serializers.CharField(source='producto.descripcion')
#    dimensiones = serializers.CharField(source='producto.dimensiones')
#    material = serializers.CharField(source='producto.material')
#    disponible = serializers.CharField(source='producto.disponible')
#    titulo = serializers.CharField(source='producto.titulo')
#    thumbnail = serializers.CharField(source='producto.thumbnail')

#   class Meta:
#        model = BodegaProducto
#        fields = ('id', 'producto', 'bodega', 'cantidad', 'estado', 'item', 'subcategoria', 'categoria',
#                  'peso', 'precio', 'descripcion', 'dimensiones', 'material', 'disponible', 'titulo', 'thumbnail')

class AdminProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProducto
        fields = '__all__'

class AdminItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminItem
        fields = '__all__'

###
class ItemFullSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(required=False)
    class Meta:
        model = Item
        fields = '__all__'

class ProductoFullSerializer(serializers.ModelSerializer):
    item= ItemFullSerializer(required=False)
    categoria = CategoriaSerializer(required=False)
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoCategoriaSubcategoriaSerializer(serializers.ModelSerializer):
    subcategoria= SubcategoriaSerializer(required=False)
    categoria = CategoriaSerializer(required=False)
    bodega = BodegaCiudadSerializer(required=False)
    class Meta:
        model = Producto
        fields = '__all__'


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'


class FacturaFullSerializer(serializers.ModelSerializer):
    estadoCompra = serializers.CharField(source='estado.estado')
    direccion = serializers.CharField(source='carro.usuario.address')
    ciudad = serializers.CharField(source='carro.usuario.ciudad.nombre')
    totalCompra = serializers.IntegerField(source='carro.totalProduct')
    pago = serializers.CharField(source='metodoPago.tipo')
    comprador = serializers.CharField(source='carro.usuario.name')
    updated = serializers.DateTimeField(source='estado.dateUpdated')
    class Meta:
        model = Factura
        fields = '__all__'
    
class CarroProductoFullSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='producto.titulo')
    precio = serializers.DecimalField(source='producto.precio', max_digits=5, decimal_places=2)
    subtotal = serializers.DecimalField(source='carro.subtotal', max_digits=5, decimal_places=2)
    

    class Meta:
        model = CarroProducto
        fields = '__all__'