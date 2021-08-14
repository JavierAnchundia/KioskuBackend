from django.db.models.expressions import Subquery
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import  * 
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse
import base64
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.db.models import Max

# Create your views here.

class CiudadView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        cityObj = Ciudad.objects.all()
        serializer = CiudadSerializer(cityObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CiudadViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Ciudad.objects.get(id=pk)
        except Ciudad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cityObj = self.get_object(pk)
        serializer = CiudadSerializer(cityObj)
        return Response(serializer.data, status=status.HTTP_200)

    def put(self, request, pk, format=None):
        cityObj = self.get_object(pk)
        serializer = CiudadSerializer(cityObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cityObj = self.get_object(pk)
        cityObj.delete()
        return Response(status=status.HTTP_200_OK)


class ProvinciaView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        provObj = Provincia.objects.all()
        serializer = ProvinciaSerializer(provObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProvinciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProvinciaViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Provincia.objects.get(id=pk)
        except Provincia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        provObj = self.get_object(pk)
        serializer = ProvinciaSerializer(provObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        provObj = self.get_object(pk)
        serializer = ProvinciaSerializer(provObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        provObj = self.get_object(pk)
        provObj.delete()
        return Response(status=status.HTTP_200_OK)


class MembresiaView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        membObj = Membresia.objects.all()
        serializer = MembresiaSerializer(membObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MembresiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembresiaViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Membresia.objects.get(id=pk)
        except Membresia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        membObj = self.get_object(pk)
        serializer = MembresiaSerializer(membObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        membObj = self.get_object(pk)
        serializer = MembresiaSerializer(membObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        membObj = self.get_object(pk)
        membObj.delete()
        return Response(status=status.HTTP_200_OK)

'''API PARA OBTENER Y EDITAR USUARIOS'''
class UsuarioViewGet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        usuarioObj = self.get_object(email)
        serializer = UserFullSerializer(usuarioObj)
        return Response(serializer.data)

    def put(self, request, email, format = None):
        
        usuarioObj = self.get_object(email)
        serializer = UserFullSerializer(usuarioObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if 'password' in request.data:
                usuarioObj.set_password(request.data['password'])
                usuarioObj.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''API PARA OBTENER INFORMACION DE UN USUARIO'''
class UsuarioView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        usuarioObj = self.get_object(pk)
        serializer = UserFullSerializer(usuarioObj)
        return Response(serializer.data)
    def put(self, request, pk, format = None):
        print(request.data)
        usuarioObj = self.get_object(pk)
        serializer = UserProfileSerializer(usuarioObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if 'password' in request.data:
                usuarioObj.set_password(request.data['password'])
                usuarioObj.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''API PARA CREAR UN USUARIO'''
class UsuarioCrear(APIView):
    #permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        catObj = Categoria.objects.all().order_by('nombre')
        serializer = CategoriaSerializer(catObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Categoria.objects.get(id=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        catObj = self.get_object(pk)
        serializer = CategoriaSerializer(catObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        catObj = self.get_object(pk)
        serializer = CategoriaSerializer(catObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        catObj = self.get_object(pk)
        catObj.delete()
        return Response(status=status.HTTP_200_OK)


class SubcategoriaView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        subcatObj = Subcategoria.objects.all()
        serializer = SubcategoriaSerializer(subcatObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubcategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubcategoriaViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Subcategoria.objects.get(id=pk)
        except Subcategoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subcatObj = self.get_object(pk)
        serializer = SubcategoriaSerializer(subcatObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subcatObj = self.get_object(pk)
        serializer = SubcategoriaSerializer(subcatObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subcatObj = self.get_object(pk)
        subcatObj.delete()
        return Response(status=status.HTTP_200_OK)

class SubcategoriaCategoriaView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Subcategoria.objects.filter(categoria_id=pk)
        except Subcategoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subcatObj = self.get_object(pk)
        serializer = SubcategoriaSerializer(subcatObj, many=True)
        return Response(serializer.data)

class BodegaView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        bodeObj = Bodega.objects.all()
        serializer = BodegaSerializer(bodeObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BodegaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BodegaCiudadView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        bodeObj = Bodega.objects.all()
        serializer = BodegaCiudadSerializer(bodeObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BodegaCiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\

class BodegaItemView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        bodeItemObj = BodegaItem.objects.all()
        serializer = BodegaItemSerializer(bodeItemObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BodegaItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\

class BodegaItemViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return BodegaItem.objects.get(id=pk)
        except BodegaItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bodeItemObj = self.get_object(pk)
        serializer = BodegaItemSerializer(bodeItemObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bodeItemObj = self.get_object(pk)
        serializer = BodegaItemSerializer(bodeItemObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bodeItemObj = self.get_object(pk)
        bodeItemObj.delete()
        return Response(status=status.HTTP_200_OK)

class BodegaViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Bodega.objects.get(id=pk)
        except Bodega.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bodeObj = self.get_object(pk)
        serializer = BodegaSerializer(bodeObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bodeObj = self.get_object(pk)
        serializer = BodegaSerializer(bodeObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bodeObj = self.get_object(pk)
        bodeObj.delete()
        return Response(status=status.HTTP_200_OK)


class BodegaCiudadViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Bodega.objects.get(id=pk)
        except Bodega.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bodeObj = self.get_object(pk)
        serializer = BodegaCiudadSerializer(bodeObj)
        return Response(serializer.data)

class CarroComprasView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        ccObj = CarroCompras.objects.all()
        serializer = CarroComprasSerializer(ccObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarroComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarroComprasViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return CarroCompras.objects.get(user=pk)
        except CarroCompras.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ccObj = self.get_object(pk)
        serializer = CarroComprasSerializer(ccObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ccObj = self.get_object(pk)
        serializer = CarroComprasSerializer(ccObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ccObj = self.get_object(pk)
        ccObj.delete()
        return Response(status=status.HTTP_200_OK)

class EstadoView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        stateObj = Estado.objects.all()
        serializer = EstadoSerializer(stateObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstadoIdView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, estado):
        try:
            return Estado.objects.filter(estado=estado)[0]
        except Estado.DoesNotExist:
            raise Http404

    def get(self, request, estado, format=None):
        stateObj = self.get_object(estado)
        serializer = EstadoSerializer(stateObj)
        return Response(serializer.data)


class EstadoViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Estado.objects.get(id=pk)
        except Estado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stateObj = self.get_object(pk)
        serializer = EstadoSerializer(stateObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stateObj = self.get_object(pk)
        serializer = EstadoSerializer(stateObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stateObj = self.get_object(pk)
        stateObj.delete()
        return Response(status=status.HTTP_200_OK)

class ItemView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        itemObj = Item.objects.all()
        serializer = ItemSerializer(itemObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemUnassignedView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        estado = Estado.objects.filter(estado='Por Evaluar')
        adminItem = AdminItem.objects.all()

        itemsUnassigned = Item.objects.exclude(id__in= adminItem.values_list("item", flat=True))\
            .filter(estado__in=estado.values_list("id", flat=True))
        serializer = ItemSerializer(itemsUnassigned, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemAssignedView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            adminItem = AdminItem.objects.filter(admin=pk)
            return Item.objects.filter(id__in=adminItem.values_list("item", flat=True))
        except Estado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        itemsUnassigned = self.get_object(pk)
        serializer = ItemEstadoSerializer(itemsUnassigned, many=True)
        return Response(serializer.data)

class ItemsUserAcceptedView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        estado = Estado.objects.filter(estado='Aceptado')
        producto = Producto.objects.all()

        # Esto esta filtrando a los items que no hayan sido usados para crear algun producto y tambien aquellos que tengan el estado como "Aceptado por parte del usuario"
        itemsUserAccepted = Item.objects.exclude(id__in=producto.values_list("item", flat=True))\
            .filter(estado__in=estado.values_list("id", flat=True))

        serializer = ItemSerializer(itemsUserAccepted, many=True)
        return Response(serializer.data)



class AdminItemView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        adminItemObj = AdminItem.objects.all()
        serializer = AdminItemSerializer(adminItemObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminItemSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Item.objects.get(id=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        itemObj = self.get_object(pk)
        serializer = ItemSerializer(itemObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        itemObj = self.get_object(pk)
        serializer = ItemSerializer(itemObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        itemObj = self.get_object(pk)
        imagenItem = ImagenItem.objects.filter(item=pk)
        serializer = ImagenItemSerializer(imagenItem, many=True)
        for ser in serializer.data:
            print(ser)
            if(ser['imagen'] is not None):
                path = ser['imagen'][7:]
                default_storage.delete(path)
            else:
                return Response(status=status.HTTP_200_OK)
        itemObj.delete()
        return Response(status=status.HTTP_200_OK)

# Funciones auxiliares
def convertImages(request):
    images = []
    if len(request.data['imagesList']) >= 1:
        for req in request.data['imagesList']:
            if(req['imagen']):
                format, imgstr = req['imagen'].split(';base64,')
                ext = format.split('/')[-1]
                imag = ContentFile(base64.b64decode(imgstr), name='img_'+ req['name'])
                data = {
                    'item': req['item'],
                    'imagen': imag
                }
                images.append(data)
    return images

class ImagenItemView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        itemObj = ImagenItem.objects.all()
        serializer = ImagenItemSerializer(itemObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = convertImages(request)
        serializer = ImagenItemSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            Item.objects.filter(id=serializer.data[0]['item']).update(thumbnail=serializer.data[0]['imagen'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImagenItemViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return ImagenItem.objects.filter(item=pk)
        except ImagenItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        itemObj = self.get_object(pk)
        serializer = ImagenItemSerializer(itemObj,many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        itemObj = self.get_object(pk)
        serializer = ImagenItemSerializer(itemObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        itemObj = self.get_object(pk)
        serializer = ImagenItemSerializer(itemObj)
        if(serializer['imagen'].value is not None):
            path = serializer['imagen'].value[7:]
            default_storage.delete(path)
        else:
            return Response(status=status.HTTP_200_OK)
        itemObj.delete()
        return Response(status=status.HTTP_200_OK)

class ProductoView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        prodObj = Producto.objects.all()
        serializer = ProductoSerializer(prodObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Producto.objects.get(id=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        serializer = ProductoFullSerializer(prodObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        serializer = ProductoSerializer(prodObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        imagenProd = ImagenProducto.objects.filter(producto=pk)
        serializer = ImagenProductoSerializer(imagenProd, many=True)
        for ser in serializer.data:
            if(ser['imagen'] is not None):
                path = ser['imagen'][7:]
                print(path)
                default_storage.delete(path)
            else:
                return Response(status=status.HTTP_200_OK)
        prodObj.delete()
        return Response(status=status.HTTP_200_OK)


class ImagenProductoView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        prodObj = ImagenProducto.objects.all()
        serializer = ImagenProductoSerializer(prodObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = convertImages(request)
        serializer = ImagenProductoSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            Producto.objects.filter(id=serializer.data[0]['producto']).update(thumbnail=serializer.data[0]['imagen'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImagenProductoViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return ImagenProducto.objects.filter(producto=pk)
        except ImagenProducto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        serializer = ImagenProductoSerializer(prodObj, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        serializer = ImagenProductoSerializer(prodObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        serializer = ImagenProductoSerializer(prodObj)
        if(serializer['imagen'].value is not None):
            path = serializer['imagen'].value[7:]
            default_storage.delete(path)
        else:
            return Response(status=status.HTTP_200_OK)
        prodObj.delete()
        return Response(status=status.HTTP_200_OK)


class MembresiaView(APIView):
    def get(self, request, format=None):
        memObj = Membresia.objects.all()
        serializer = MembresiaSerializer(memObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MembresiaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MembresiaViewSet(APIView):
    def get_object(self, pk):
        try:
            return Membresia.get(id=pk)
        except Membresia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        memObj = self.get_object(pk)
        serializer = MembresiaSerializer(memObj, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        memObj = self.get_object(pk)
        serializer = MembresiaSerializer(memObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        memObj = self.get_object(pk)
        memObj.delete()
        return Response(status=status.HTTP_200_OK)

class AnuncioView(APIView):
    def get(self, request, format=None):
        anunObj = Anuncio.objects.all()
        serializer = AnuncioSerializer(anunObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnuncioSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnuncioViewSet(APIView):
    def get_object(self, pk):
        try:
            return Anuncio.get(id=pk)
        except Anuncio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        anunObj = self.get_object(pk)
        serializer = AnuncioSerializer(anunObj, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        anunObj = self.get_object(pk)
        serializer = AnuncioSerializer(anunObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        anunObj = self.get_object(pk)
        anunObj.delete()
        return Response(status=status.HTTP_200_OK)

    
### VISTAS ESPECIALES ##

class getItemByUser(APIView):
    def get(self, request, id):
        
        items = Item.objects.filter(propietario=id).order_by('-id')
        page_number = request.GET.get('page', 1)
        page_size = int(request.GET.get('size', 2))
        paginator = Paginator(items , page_size)
        serializer = ItemFullSerializer(paginator.page(page_number) , many=True, context={'request':request})
        response = Response([serializer.data, len(items)], status=status.HTTP_200_OK)
        return response


class getSubcategoriesByCat(APIView):
    def get(self, request, id):
        subcat = Subcategoria.objects.filter(categoria=id).order_by('nombre')
        serializer = SubcategoriaSerializer(subcat, many= True)
        return Response(serializer.data)

class getMostRecentProducts(APIView):
    def get(self, request):
        prod = Producto.objects.all().order_by('-id')[:30]
        serializer = ProductoFullSerializer(prod, many=True)
        imagen = ImagenProducto.objects.all()
        imgSerializer = ImagenProductoSerializer(imagen, many=True)
        return HttpResponse(json.dumps([serializer.data, imgSerializer.data], cls=DjangoJSONEncoder))

class getProductsByCategory(APIView):
    def get(self, request, id):
        prod = Producto.objects.filter(categoria=id).order_by('-id')
        imagen = ImagenProducto.objects.filter(producto__categoria=id)
        imgSerializer = ImagenProductoSerializer(imagen, many=True)
        serializer = ProductoSerializer(prod, many=True)
        return HttpResponse(json.dumps([serializer.data, imgSerializer.data], cls=DjangoJSONEncoder))
 
class getProductsBySubCategory(APIView):
    def get(self, request, pk):
        prod = Producto.objects.filter(subcategoria=pk).order_by('-pk')
        imagenItem = ImagenProducto.objects.filter(producto__subcategoria=pk)
        imgSerializer = ImagenProductoSerializer(imagenItem, many=True)
        serializer = ProductoSerializer(prod, many=True)
        return HttpResponse(json.dumps([serializer.data, imgSerializer.data], cls=DjangoJSONEncoder))


class createCarroCompras(APIView):
    def post(self, request, format=None):
        serializer = ImagenProductoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getCarroByUser(APIView):
    def get(self, request, pk):
        obj = CarroCompras.get(usuario=pk)
        serializer = CarroCompras(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class getCitiesByProv(APIView):
    def get(self, request, pk):
        obj = Ciudad.objects.filter(provincia=pk)
        serializer = CiudadSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class updateCredits(APIView):

    def patch(self, request, pk):
        print(request.data)
        model = User.objects.get(id=pk)
        data = {"saldo": model.saldo + int(request.data['creditos'])}
        serializer = UserProfileSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getRecentItemsForCat(APIView):
    def get(self, request): 
        qs = Categoria.objects.annotate(mostrecent=Max('producto__id')).values()
        categories = list(qs.values('mostrecent'))
        products = []
        for id in categories:
            if(id['mostrecent']!= None):
                products.append(id['mostrecent'])        
        qs2 = Producto.objects.filter(id__in=products)
        serializer = ProductoFullSerializer(qs2, many= True)
        return Response(serializer.data)
