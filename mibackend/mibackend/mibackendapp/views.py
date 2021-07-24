from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import  * 
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse, JsonResponse
import base64
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files.base import ContentFile
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
        serializer = UserProfileSerializer(usuarioObj)
        return Response(serializer.data)
    def put(self, request, email, format = None):
        usuarioObj = self.get_object(email)
        serializer = UserProfileSerializer(usuarioObj, data=request.data, partial=True)
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
        serializer = UserProfileSerializer(usuarioObj)
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
        itemObj.delete()
        return Response(status=status.HTTP_200_OK)

# Funciones auxiliares
def convertImages(request):
    images = []
    print(len(request.data))
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImagenItemViewSet(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return ImagenItem.objects.get(id=pk)
        except ImagenItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        itemObj = self.get_object(pk)
        serializer = ImagenItemSerializer(itemObj)
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
        itemObj.delete()
        return Response(status=status.HTTP_200_OK)


### VISTAS ESPECIALES ##

class getItemByUser(APIView):
    def get(self, request, id):
        items = Item.objects.filter(propietario=id)
        imagenItem = ImagenItem.objects.filter(item__propietario=id)
        serializer = ImagenItemSerializer(imagenItem, many=True)
        itemSer = ItemFullSerializer(items, many=True)
        return HttpResponse(json.dumps([serializer.data, itemSer.data], cls=DjangoJSONEncoder))

class getSubcategoriesByCat(APIView):
    def get(self, request, id):
        subcat = Subcategoria.objects.filter(categoria=id).order_by('nombre')
        serializer = SubcategoriaSerializer(subcat, many= True)
        return Response(serializer.data)

class getMostRecentProducts(APIView):
    def get(self, request):
        prod = Producto.objects.all().order_by('-pk')[:30]
        serializer = ProductoSerializer(prod, many=True)
        return HttpResponse(json.dumps([serializer.data], cls=DjangoJSONEncoder))

class getProductsByCategory(APIView):
    def get(self, request, pk):
        prod = Producto.objects.filter(categoria=pk).order_by('-pk')
        serializer = ProductoSerializer(prod, many=True)
        return HttpResponse(json.dumps([serializer.data], cls=DjangoJSONEncoder))
 