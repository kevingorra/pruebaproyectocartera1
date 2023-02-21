from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

# Create your views here.

def busqueda(request1):

<<<<<<< HEAD
    return render(request1,"busqueda.html")
=======
    return render(request1,"nits/busqueda.html")
>>>>>>> 4f004a043a08597b91294d4c16b79dcb59c45bba

def buscar(request1):
    mensaje="Articulo Buscado : %r" %request1.GET["prd"]
    

    return HttpResponse(mensaje)
<<<<<<< HEAD
def vista2(request):
    return render(request,'vista2.html')


def vista1(request):
    return render(request,'vista1.html')

def Home(request):
    return render(request,'tabla.html')
=======

def Home(request):
    return render(request,'nits/login.html')
>>>>>>> 4f004a043a08597b91294d4c16b79dcb59c45bba

def tabla_indicadores(request):

    """Leer el nit y mostrar la tabla de Maestro"""
    
    nit = request.GET["prd"]
    maestro = pd.read_csv(
<<<<<<< HEAD
        r'C:\Users\KEVIN\Desktop\PruebaProyectoCartera\MaestroSubir.csv',
        sep=";")
    maestro = maestro.astype({'NIT': str})
=======
        r'D:\Users\p.manufactura07\OneDrive - Centro de Servicios Mundial SAS\Escritorio\PruebaProyectoCartera\PythonMaestro7.csv',
        sep=",")
    maestro = maestro.astype({'NIT': str})
    print(maestro)
>>>>>>> 4f004a043a08597b91294d4c16b79dcb59c45bba
    tabla = maestro[maestro.NIT == nit]
    
  
    if tabla.shape[0] == 0:
        pedazo_html = "<h1>Ese NIT no está en la tabla</h1>"
    else:
        pedazo_html = tabla.T.to_html(index=False,classes=['maestro'])
    

<<<<<<< HEAD
    return render(request, "index.html", {'tabla_a_mostrar': pedazo_html, 'nit': nit})
=======
    return render(request, "nits/index.html", {'tabla_a_mostrar': pedazo_html, 'nit': nit})
>>>>>>> 4f004a043a08597b91294d4c16b79dcb59c45bba


