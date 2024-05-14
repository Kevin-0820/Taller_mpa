from datetime import date
from django.shortcuts import render
from .models import Productos, CambioStock
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')


def list_productos(request):
    Producto=list(Productos.objects.values())
    data={'Producto':Producto}
    return JsonResponse(data)


def insertar_o_actualizar(request): 
    if request.method == 'POST':
        Producto = int(request.POST['Producto'])
        Cantidad = int(request.POST['Cantidad'])
        Comentario = request.POST['Comentario']
        Fecha = request.POST['Fecha']
        TipoCambio = request.POST['TipoCambio']
        
        if TipoCambio == "Egreso":
            Cantidad=-Cantidad
        
        producto = Productos.objects.get(id=Producto)
        producto.Cantidad += Cantidad
        producto.save()
        
        cambio_stock = CambioStock(id_producto_id=Producto, cantidad=Cantidad, tipo_cambio=TipoCambio, comentario=Comentario, fecha_c=Fecha)
        cambio_stock.save()
        

        return redirect('index')
    else:
        return render(request, 'index.html')
    
    