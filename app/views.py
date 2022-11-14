from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def pacientes(request):
    return render(request, 'app/pacientes.html')

def doctores(request):
    return render(request, 'app/doctores.html')

def citas(request):
    return render(request, 'app/citas.html')

def pagos(request):
    return render(request, 'app/pagos.html')
    