from django.urls import path, include
from .views import *
from rest_framework import routers

# CREAMOS LAS RUTAS PARA LA API
router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('tipoproductos', TipoProductoViewset)

## SE VAN A CREAR TODAS LAS URLS 
urlpatterns = [
    # API
    path('api/', include(router.urls)),

    path('', index, name="index"),
    path('indexapi/', indexapi, name="indexapi"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('cart/', cart, name="cart"),
    path('contact/', contact, name="contact"),
    path('shop/', shop, name="shop"),
    path('checkout/', checkout, name="checkout"),
    path('wishlist/', wishlist, name="wishlist"),
    path('productsingle/', productsingle, name="productsingle"),
    
    #CRUD
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
]

