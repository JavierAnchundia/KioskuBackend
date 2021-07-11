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
        models = Membresia
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
            'is_active'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.email = validated_data.get('email')
        user.set_password(password)
        user.save()
        return user

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Subcategoria
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'

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

class AdminProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProducto
        fields = '__all__'

class AdminItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminItem
        fields = '__all__'
