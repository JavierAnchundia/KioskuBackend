from django.db.models.aggregates import Count, Sum
from rest_framework.fields import ImageField
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
from django.db.models import Max, F
from django.utils import timezone
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
            Bodega.objects.filter(id=serializer.data['id'])\
                .update(nombre=(Ciudad.objects.get(id=serializer.data['ciudad']).siglas + '-'
                                + '{0:03}'.format(serializer.data['id'])))

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

class BodegaCiudadActivasView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        bodeObj = Bodega.objects.filter(is_active=True)
        serializer = BodegaCiudadSerializer(bodeObj, many=True)
        return Response(serializer.data)

class BodegaCiudadActivasViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Bodega.objects.get(Q(id=pk), Q(is_active=True))
        except Bodega.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bodeObj = self.get_object(pk)
        serializer = BodegaCiudadSerializer(bodeObj)
        return Response(serializer.data)

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

#class BodegaProductoView(APIView):
#    #permission_classes = (IsAuthenticated,)
#    def get(self, request, format=None):
#        bodeProductoObj = BodegaProducto.objects.all()
#        serializer = BodegaProductoSerializer(bodeProductoObj, many=True)
#        return Response(serializer.data)

#   def post(self, request, format=None):
#        serializer = BodegaProductoSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\

#class BodegaProductoViewSet(APIView):
#    #permission_classes = (IsAuthenticated,)
#    def get_object(self, pk):
#        try:
#            return BodegaProducto.objects.get(id=pk)
#        except BodegaProducto.DoesNotExist:
#            raise Http404

#    def get(self, request, pk, format=None):
#        bodeProductoObj = self.get_object(pk)
#        serializer = BodegaProductoSerializer(bodeProductoObj)
#        return Response(serializer.data)

#    def put(self, request, pk, format=None):
#        bodeProductoObj = self.get_object(pk)
#        serializer = BodegaProductoSerializer(bodeProductoObj, data=request.data, partial=True)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, pk, format=None):
#        bodeProductoObj = self.get_object(pk)
#        bodeProductoObj.delete()
#        return Response(status=status.HTTP_200_OK)


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
            Bodega.objects.filter(id=serializer.data['id']) \
                .update(nombre=(Ciudad.objects.get(id=serializer.data['ciudad']).siglas + '-'
                                + '{0:03}'.format(serializer.data['id'])))
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
            estados = Estado.objects.filter(estado=estado)
            if(estados):

                return estados[0]
            else:
                raise Http404

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
                imag = ContentFile(base64.b64decode(imgstr), name='img_'+ req['name'] + '.jpg')
                data = {
                    'item': req['item'],
                    'imagen': imag
                }
                images.append(data)
    return images

def convertImagesProduct(request):
    images = []
    if len(request.data['imagesList']) >= 1:
        for req in request.data['imagesList']:
            if(req['imagen']):
                format, imgstr = req['imagen'].split(';base64,')
                ext = format.split('/')[-1]
                imag = ContentFile(base64.b64decode(imgstr), name='img_'+ req['name']+ '.jpg')
                data = {
                    'producto': req['producto'],
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

class ProductoCategoriaSubcategoriaViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Producto.objects.get(id=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        serializer = ProductoCategoriaSubcategoriaSerializer(prodObj)
        return Response(serializer.data)

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
        print(request.data)
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
        data = convertImagesProduct(request)
        serializer = ImagenProductoSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            if(data):
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

class ImagenIndividualProductoViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return ImagenProducto.objects.get(id=pk)
        except ImagenProducto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prodObj = self.get_object(pk)
        serializer = ImagenProductoSerializer(prodObj)
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
        memObj = Membresia.objects.filter(active=True)
        serializer = MembresiaSerializer(memObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MembresiaSerializer(data=request.data)
        if serializer.is_valid():         
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MembresiaViewSet(APIView):
    def get_object(self, pk):
        try:
            return Membresia.objects.get(id=pk)
        except Membresia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        memObj = self.get_object(pk)
        serializer = MembresiaSerializer(memObj)
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
        serializer = AnuncioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnuncioViewSet(APIView):
    def get_object(self, pk):
        try:
            return Anuncio.objects.get(id=pk)
        except Anuncio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        anunObj = self.get_object(pk)
        serializer = AnuncioSerializer(anunObj)
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
        ser = AnuncioSerializer(anunObj);
        if(ser.data['banner'] is not None):
            path = ser.data['banner'][7:]
            default_storage.delete(path)
        anunObj.delete()
        return Response(status=status.HTTP_200_OK)

class FacturaView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        factObj = Factura.objects.filter(detalle='item')
        serializer = FacturaFullSerializer(factObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            productos = CarroProducto.objects.filter(carro=serializer.data['carro'])
            updateProductStock(productos)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacturaViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Factura.objects.get(id=pk)
        except Factura.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        factObj = self.get_object(pk)
        serializer = FacturaSerializer(factObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        factObj = self.get_object(pk)
        serializer = FacturaSerializer(factObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        factObj = self.get_object(pk)
        factObj.delete()
        return Response(status=status.HTTP_200_OK)

class CarroComprasView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        cartObj = CarroCompras.objects.all()
        serializer = CarroComprasSerializer(cartObj, many=True)
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
            return CarroCompras.objects.get(id=pk)
        except CarroCompras.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cartObj = self.get_object(pk)
        serializer = CarroComprasSerializer(cartObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cartObj = self.get_object(pk)
        serializer = CarroComprasSerializer(cartObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cartObj = self.get_object(pk)
        cartObj.delete()
        return Response(status=status.HTTP_200_OK)

class CarroProductoView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        cartObj = CarroProducto.objects.all()
        serializer = CarroProductoSerializer(cartObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarroProductoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            calcularTarifaEntrega(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def calcularTarifaEntrega(carroProductoList):

    tarifa_total = 0
    tarifa_entrega = TarifaEntrega.objects.all().first()

    for p in carroProductoList:

        ciudad_bodega = Ciudad.objects.get(id=Bodega.objects.get(id=Producto.objects.get(id=p['producto']).bodega.id).ciudad.id)
        provincia_bodega = Provincia.objects.get(id=ciudad_bodega.provincia.id)

        usuario = User.objects.get(id=CarroCompras.objects.get(id=p['carro']).usuario.id)
        ciudad_usuario = Ciudad.objects.get(id=usuario.ciudad.id)
        provincia_usuario = Provincia.objects.get(id=ciudad_bodega.provincia.id)


        carroCompra = CarroCompras.objects.filter(id=p['carro'])

        if (ciudad_bodega and provincia_bodega and ciudad_usuario and provincia_usuario and tarifa_entrega):
            if(ciudad_bodega.id == ciudad_usuario.id):
                tarifa_total += tarifa_entrega.mismaCiudad * int(p['cantidad'])
            elif(provincia_bodega.id == provincia_usuario.id):
                tarifa_total += tarifa_entrega.difCiudadMismaProvincia * int(p['cantidad'])
            else:
                tarifa_total += tarifa_entrega.difProvincia * int(p['cantidad'])

        else:
            raise Http404

    carroCompra.update(costoEntrega = tarifa_total)
    print('success')

class CarroProductoViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return CarroProducto.objects.get(id=pk)
        except CarroProducto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cartObj = self.get_object(pk)
        serializer = CarroProductoSerializer(cartObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cartObj = self.get_object(pk)
        serializer = CarroProductoSerializer(cartObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cartObj = self.get_object(pk)
        cartObj.delete()
        return Response(status=status.HTTP_200_OK)
    
class MetodoPagoView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        pagoObj = MetodoPago.objects.all()
        serializer = MetodoPagoSerializer(pagoObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MetodoPagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MetodoPagoViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return MetodoPago.objects.get(id=pk)
        except MetodoPago.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pagoObj = self.get_object(pk)
        serializer = MetodoPagoSerializer(pagoObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pagoObj = self.get_object(pk)
        serializer = MetodoPagoSerializer(pagoObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pagoObj = self.get_object(pk)
        pagoObj.delete()
        return Response(status=status.HTTP_200_OK)


class EstadoCompraView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        estObj = EstadoCompra.objects.all()
        serializer = EstadoCompraSerializer(estObj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstadoCompraViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return EstadoCompra.objects.get(id=pk)
        except EstadoCompra.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        estObj = self.get_object(pk)
        serializer = EstadoCompraSerializer(estObj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        estObj = self.get_object(pk)
        serializer = EstadoCompraSerializer(estObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        estObj = self.get_object(pk)
        estObj.delete()
        return Response(status=status.HTTP_200_OK)


class TarifaEntregaView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        tarifaEntregaObj = TarifaEntrega.objects.all()
        if(tarifaEntregaObj):
            serializer = TarifaEntregaSerializer(tarifaEntregaObj[0])
            return Response(serializer.data)
        else:
            raise Http404


    def put(self, request, format=None):
        tarifaEntregaObj = self.get()

        serializer = TarifaEntregaSerializer(tarifaEntregaObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### VISTAS ESPECIALES ##
def updateProductStock(productos):
    serializer = CarroProductoSerializer(productos, many=True)
    for p in serializer.data:
        Producto.objects.filter(id = p['producto']).update(cantidad=(F('cantidad') - int(p['cantidad'])))

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
        prod = Producto.objects.filter(cantidad__gt=0).order_by('-id')[:30]
        serializer = ProductoFullSerializer(prod, many=True)
        imagen = ImagenProducto.objects.all()
        imgSerializer = ImagenProductoSerializer(imagen, many=True)
        return HttpResponse(json.dumps([serializer.data, imgSerializer.data], cls=DjangoJSONEncoder))

class getProductsByCategory(APIView):
    def get(self, request, id):
        prod = Producto.objects.filter(cantidad__gt=0).filter(categoria=id).order_by('-id')
        imagen = ImagenProducto.objects.filter(producto__categoria=id)
        imgSerializer = ImagenProductoSerializer(imagen, many=True)
        serializer = ProductoSerializer(prod, many=True)
        return HttpResponse(json.dumps([serializer.data, imgSerializer.data], cls=DjangoJSONEncoder))
 
class getProductsBySubCategory(APIView):
    def get(self, request, pk):
        prod = Producto.objects.filter(cantidad__gt=0).filter(subcategoria=pk).order_by('-pk')
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

class getInvoiceByUser(APIView):
    def get(self, request, pk):
        qs = Factura.objects.filter(carro__usuario=pk)
        serializer = FacturaFullSerializer(qs, many= True)
        return Response(serializer.data)

class getStatistics(APIView):
    def get(self, request):
        users = User.objects.aggregate(totalUsers=Count("id"))
        orders = Factura.objects.filter(dateCreated__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).aggregate(totalOrders = Count("id"))
        submissions = Item.objects.filter(estado__date_updated__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).aggregate(totalSubs=Count("id"))
        pending = Factura.objects.filter(estado__estado="Por entregar").filter(dateCreated__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).aggregate(totalPending=Count("id"))

        return HttpResponse(json.dumps([users,orders, submissions, pending], cls=DjangoJSONEncoder))

class getDailyTotalOrders(APIView):
    def get(self, request):
        orders = Factura.objects.filter(dateCreated__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).values('dateCreated').annotate(count = Count('id')).order_by('dateCreated').values("dateCreated", "count")
        return HttpResponse(json.dumps(list(orders), cls=DjangoJSONEncoder))

class getRecentItems(APIView):
    def get(self, request):
        item = Item.objects.filter(cantidad__gt=0).order_by('-id')[:5]
        serializer = ItemFullSerializer(item, many=True)
        return Response(serializer.data)

class getOrderDetail(APIView):
    def get(self, request, pk):
        productos = CarroProducto.objects.filter(carro=pk)
        serializer = CarroProductoFullSerializer(productos, many= True)

        return Response(serializer.data)

class getOrdersPending(APIView):
    def get(self, request):
        ordenes = Factura.objects.filter(detalle="item").filter(estado__estado="Por Entregar").filter(estado__transportista__isnull=True)
        serializer = FacturaFullSerializer(ordenes, many=True)
        return Response(serializer.data)

class getMyDeliveries(APIView):
    def get(self, request, pk):
        ordenes = Factura.objects.filter(detalle="item").filter(estado__transportista__id=pk)
        serializer = FacturaFullSerializer(ordenes, many=True)
        return Response(serializer.data)
