from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Habitacion
from .forms import HabitacionForm 
from .models import Cliente
from .forms import ClienteForm
from .models import Reserva
from .forms import ReservaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Mostrar todas las habitaciones
def lista_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitaciones/lista.html', {'habitaciones': habitaciones})

# Crear una nueva habitación
def crear_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_habitaciones')
    else:
        form = HabitacionForm()
    return render(request, 'habitaciones/formulario.html', {'form': form})

# Editar una habitación existente
def editar_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('lista_habitaciones')
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, 'habitaciones/formulario.html', {'form': form})

# Eliminar una habitación
def eliminar_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        habitacion.delete()
        return redirect('lista_habitaciones')
    return render(request, 'habitaciones/eliminar.html', {'habitacion': habitacion})


# Listar Clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

# Crear Cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/formulario.html', {'form': form})

# Editar Cliente
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/formulario.html', {'form': form})

# Eliminar Cliente
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/eliminar.html', {'cliente': cliente})

# Listar Reservas
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista.html', {'reservas': reservas})

# Crear Reserva
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/formulario.html', {'form': form})

# Editar Reserva
def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/formulario.html', {'form': form})

# Eliminar Reserva
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'reservas/eliminar.html', {'reserva': reserva})