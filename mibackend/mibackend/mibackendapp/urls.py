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
    path('subcategoriacategoria/<str:pk>/', views.SubcategoriaCategoriaView.as_view()),
    path('bodegasciudad/', views.BodegaCiudadView.as_view()),
    path('bodega-item/', views.BodegaItemView.as_view()),
    path('bodega-item/<str:pk>/', views.BodegaItemViewSet.as_view()),
    #path('bodega-producto/', views.BodegaProductoView.as_view()),
    #path('bodega-producto/<str:pk>/', views.BodegaProductoViewSet.as_view()),

    path('bodegasciudad/<str:pk>/', views.BodegaCiudadViewSet.as_view()),
    path('bodegasciudadactivas/<str:pk>/', views.BodegaCiudadActivasViewSet.as_view()),
    path('bodegasciudadactivas/', views.BodegaCiudadActivasView.as_view()),

    path('item/<str:pk>/', views.ItemViewSet.as_view()),
    path('item/', views.ItemView.as_view()),
    path('img-item/<str:pk>/', views.ImagenItemViewSet.as_view()),
    path('img-item/', views.ImagenItemView.as_view()),
    path('estado/<str:pk>/', views.EstadoViewSet.as_view()),
    path('estado/', views.EstadoView.as_view()),
    path('estado-id/<str:estado>/', views.EstadoIdView.as_view()),
    path('producto/<str:pk>/', views.ProductoViewSet.as_view()),
    path('producto/', views.ProductoView.as_view()),
    path('producto-categoria-subcategoria/<str:pk>/', views.ProductoCategoriaSubcategoriaViewSet.as_view()),

    path('tarifa-entrega/', views.TarifaEntregaView.as_view()),

    path('img-producto/', views.ImagenProductoView.as_view()),
    path('img-producto/<str:pk>/', views.ImagenProductoViewSet.as_view()),
    path('img-producto-individual/<str:pk>/', views.ImagenIndividualProductoViewSet.as_view()),


    path('shopping-cart/', views.createCarroCompras.as_view()),
    path('shopping-cart/<str:pk>/', views.getCarroByUser.as_view()),
    path('membresia/', views.MembresiaView.as_view()),
    path('membresia/<str:pk>/', views.MembresiaViewSet.as_view()),
    path('anuncio/', views.AnuncioView.as_view()),
    path('anuncio/<str:pk>/', views.AnuncioViewSet.as_view()),
    path('factura/', views.FacturaView.as_view()),
    path('factura/<str:pk>/', views.FacturaViewSet.as_view()),
    path('carro-compras/', views.CarroComprasView.as_view()),
    path('carro-compras/<str:pk>/', views.CarroComprasViewSet.as_view()),
    path('carro-producto/', views.CarroProductoView.as_view()),
    path('carro-producto/<str:pk>/', views.CarroProductoViewSet.as_view()),
    path('pago/', views.MetodoPagoView.as_view()),
    path('pago/<str:pk>/', views.MetodoPagoViewSet.as_view()),
    path('estado-compra/', views.EstadoCompraView.as_view()),
    path('estado-compra/<str:pk>/', views.EstadoCompraViewSet.as_view()),

    path('itemsByUser/<str:id>/', views.getItemByUser.as_view()),
    path('itemunassigned/', views.ItemUnassignedView.as_view()),
    path('itemassigned/<str:pk>/', views.ItemAssignedView.as_view()),
    path('itemsuseraccepted/', views.ItemsUserAcceptedView.as_view()),


    path('adminItem/', views.AdminItemView.as_view()),

    path('subcatByCat/<str:id>/', views.getSubcategoriesByCat.as_view()),
    path('most-recent/', views.getMostRecentProducts.as_view()),
    path('productsByCat/<str:id>/', views.getProductsByCategory.as_view()),
    path('productsBySubcat/<str:pk>/', views.getProductsBySubCategory.as_view()),
    path('citiesByProv/<str:pk>/', views.getCitiesByProv.as_view()),
    path('update-credits/<str:pk>/', views.updateCredits.as_view()),
    path('recentItemsCat/', views.getRecentItemsForCat.as_view()),
    path('historial-compra/<str:pk>/', views.getInvoiceByUser.as_view()),
    path('statistics/', views.getStatistics.as_view()),
    path('dailyOrders/', views.getDailyTotalOrders.as_view()),
    path('recentSubmissions/', views.getRecentItems.as_view()),
    path('orderDetail/<str:pk>/', views.getOrderDetail.as_view()),
    path('ordenes-pendientes/', views.getOrdersPending.as_view()),
    path('deliveries/<str:pk>/', views.getMyDeliveries.as_view()),


]


urlpatterns = format_suffix_patterns(urlpatterns)
