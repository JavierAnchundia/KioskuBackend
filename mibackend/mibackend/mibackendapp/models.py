from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models

# Create your models here.


class Provincia(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20)


class Ciudad(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20)
    siglas = models.CharField(max_length=5)
    provincia = models.ForeignKey(
        Provincia, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):

        return (self.nombre + '-' + self.siglas + '-' + str(self.id))

class Membresia(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tipo = models.CharField(max_length=20)
    pct_dscto = models.DecimalField(max_digits=5, decimal_places=2)
    tarifa = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    valorCredito = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    active = models.BooleanField(default=True)

# Modelo de usuarios
class UsuarioManager(BaseUserManager):
    def create_user(self, email=None, name=None, password=None, rol=None):

        usuario = self.model(
            email=self.normalize_email(email),
            name=name,
            password=password,
            rol="final"
        )
        usuario.set_password(password)
        usuario.staff = True
        usuario.save()
        return usuario

    def create_superuser(self, email=None, name=None, password=None, rol="admin"):
        usuario = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
            rol=rol,
        )
        usuario.staff = True
        usuario.save()
        return usuario


class User(AbstractBaseUser):
    admin = 'admin'
    evaluador = 'evaluador'
    transportista = 'transportista'
    final = 'final'
    rol_choice = [
        (admin, 'admin'),
        (evaluador, 'evaluador'),
        (final, 'final'),
        (final, 'final')
    ]
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(('email address'), unique=True,
                              max_length=200, default=None, null=True, blank=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    rol = models.CharField(max_length=10, choices=rol_choice, default=final)
    address = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    provincia = models.ForeignKey(
        Provincia, on_delete=models.PROTECT, null=True, blank=True)
    ciudad = models.ForeignKey(
        Ciudad, on_delete=models.PROTECT, null=True, blank=True)
    membresia = models.ForeignKey(
        Membresia, on_delete=models.PROTECT, null=True, blank=True)
    celular = models.CharField(max_length=10)
    cedula = models.CharField(max_length=10)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return "{}".format(self.email)

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=25)


class Subcategoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)


class Estado(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(max_length=20)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):

        return (self.estado + str(self.id))
class Item(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    propietario = models.ForeignKey(User, on_delete=models.PROTECT)
    entrega = models.CharField(max_length=80)
    creditos = models.IntegerField(default=0)
    thumbnail = models.CharField(max_length=350, null=True, blank=True)

class ImagenItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    imagen = models.ImageField(upload_to='items', max_length=250, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Bodega(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

class BodegaItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT)
    cantidad = models.IntegerField()


class Producto(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.CharField(max_length=200)
    dimensiones = models.CharField(max_length=200)
    material = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    titulo = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=350, null=True, blank=True)
    cantidad = models.IntegerField()
    bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT)

#class BodegaProducto(models.Model):
 #   id = models.AutoField(primary_key=True, unique=True)
 #  producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
 #  bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT)
 #  cantidad = models.IntegerField()

class ImagenProducto(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    imagen = models.ImageField(upload_to='producto', max_length=250, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

class AdminItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)

class AdminProducto(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

class CarroCompras(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    totalProduct = models.IntegerField()
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20)

class CarroProducto(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    carro = models.ForeignKey(CarroCompras, on_delete=models.PROTECT)

class MetodoPago(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tipo = models.CharField(max_length=20)

class EstadoCompra(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(max_length=20)
    dateUpdated = models.DateField(auto_now=True)
    transportista = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

class Factura(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    dateCreated = models.DateField(auto_now=True)
    metodoPago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    costoEntrega = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.ForeignKey(EstadoCompra, on_delete=models.SET_NULL, null=True)
    carro = models.ForeignKey(CarroCompras, on_delete=models.PROTECT)
    detalle = models.CharField(max_length=50)
    
class Anuncio(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    dateCreated = models.DateField()
    banner = models.ImageField(upload_to='banners', max_length=250, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
