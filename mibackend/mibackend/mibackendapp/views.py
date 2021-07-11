from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import  * 
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse

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
        catObj = Categoria.objects.all()
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