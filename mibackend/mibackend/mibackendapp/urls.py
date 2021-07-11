from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mibackendapp import views


urlpatterns = [
    path('ciudad/<str:pk>/', views.CiudadViewSet.as_view()),
    path('ciudad/', views.CiudadView.as_view()),
    path('provincia/<str:pk>/', views.ProvinciaViewSet.as_view()),
    path('provincia/', views.ProvinciaView.as_view()),
    path('membresia/<str:pk>/', views.MembresiaViewSet.as_view()),
    path('membresia/', views.MembresiaView.as_view()),
    path('user/<str:pk>/', views.UsuarioView.as_view()),
    path('usuario/<str:email>/', views.UsuarioViewGet.as_view()), #URLS PARA USUARIO
    path('register/', views.UsuarioCrear.as_view()), #crear usuario
    path('categoria/<str:pk>/', views.CategoriaViewSet.as_view()),
    path('categoria/', views.CategoriaView.as_view()),
    path('subcategoria/<str:pk>/', views.SubcategoriaViewSet.as_view()),
    path('subcategoria/', views.SubcategoriaView.as_view()),
    path('bodega/<str:pk>/', views.BodegaViewSet.as_view()),
    path('bodega/', views.BodegaView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
