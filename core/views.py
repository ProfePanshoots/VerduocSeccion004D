from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import *
import requests

# CREANDO UNA CLASE QUE VA A PERMITIR LA TRANSFORMACION
class ProductoViewset(viewsets.ModelViewSet):
    #queryset = Producto.objects.filter(tipo=1)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

class TipoProductoViewset(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializers

# CONTIENE UN LISTAR DE PRODUCTOS
def index(request):
    productosAll = Producto.objects.all() # SELECT * FROM producto

    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    
    try:
        paginator = Paginator(productosAll, 8) # INDICA LA CANTIDAD DE PRODUCTOS
        productosAll = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'listado': productosAll,
        'paginator': paginator
    }

    return render(request, 'core/index.html', data)

def indexapi(request):
    respuesta = requests.get('http://127.0.0.1:8000/api/productos/')
    respuesta2 = requests.get('https://mindicador.cl/api/')
    respuesta3 = requests.get('https://rickandmortyapi.com/api/character')

    # TRANSFORMACION DEL JSON
    productos = respuesta.json()
    monedas = respuesta2.json()
    aux = respuesta3.json()
    personajes = aux['results']

    data = {
        'listado': productos,
        'moneda' : monedas,
        'personajes' : personajes,
    }

    return render(request, 'core/indexapi.html', data)

def about(request):
    return render(request, 'core/about.html')

def blog(request):
    return render(request, 'core/blog.html')

@login_required
def cart(request):
    respuesta = requests.get('https://mindicador.cl/api/dolar')
    monedas = respuesta.json()
    valor_usd = monedas['serie'][0]['valor']
    # LOGICA PARA SUMAR EL PRECIO DEL CARRITO
    valor_carrito = 20000
    # TRANSFORMAMOS DE CLP A USD
    valor_total = valor_carrito/valor_usd

    data = {
        'valor' : round(valor_total,2)
    }

    return render(request, 'core/cart.html', data)

def contact(request):
    return render(request, 'core/contact.html')

@login_required
def shop(request):
    return render(request, 'core/shop.html')

def checkout(request):
    return render(request, 'core/checkout.html')

def wishlist(request):
    return render(request, 'core/wishlist.html')

def productsingle(request):
    return render(request, 'core/product-single.html')

# CRUD
def add(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # RECIBE TODA LA INFO DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() # COMMIT, INSERT INTO .........
            #data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/add-product.html', data)


def update(request,id):
    producto = Producto.objects.get(id=id) # BUSCAMOS UN PRODUCTO POR SU ID
    data = {
        'form' : ProductoForm(instance=producto) # CARGA LA INFO EN EL FORMULARIO
    }

    if request.method == 'POST':
        # RECIBE TODA LA NUEVA INFO DEL FORMULARIO
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save() # COMMIT, UPDATE .........
            #data['msj'] = "Producto modificado correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario # ACTUALIZAR VISUALMENTE EL FORMULARIO

    return render(request, 'core/update-product.html', data)

def delete(request,id):
    producto = Producto.objects.get(id=id) # BUSCAMOS UN PRODUCTO POR SU ID
    producto.delete()

    return redirect(to="index")

