from django.shortcuts import render, redirect
from .models import Pedido
# Create your views here.

def home(request):
    pedidosListados = Pedido.objects.all()
    return render(request, "gestionPedidos.html", {"pedidos": pedidosListados})

def registrarPedido(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    pedido = Pedido.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    return redirect('/')

def edicionPedido(request, codigo):
    pedido = Pedido.objects.get(codigo=codigo)
    return render(request, "edicionPedido.html", {"pedido": pedido})

def editarPedido(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    pedido = Pedido.objects.get(codigo=codigo)
    pedido.nombre = nombre
    pedido.cantidad = cantidad
    pedido.save()

    return redirect('/')


def eliminarPedido(request, codigo):
    pedido = Pedido.objects.get(codigo=codigo)
    pedido.delete()
    return redirect('/')
    