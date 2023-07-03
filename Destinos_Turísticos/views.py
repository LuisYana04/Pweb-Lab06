from django.shortcuts import render
from django.http import HttpResponse
from .models import dest
def index(request):

    dest1 = dest()
    dest1.nombre = 'Lima'
    dest1.descripcion = 'La ciudad de los reyes'
    dest1.img = 'lima.jpg'
    dest1.precio = 700

    dest2 = dest()
    dest2.nombre = 'Arequipa'
    dest2.descripcion = 'La ciudad Blanca'
    dest2.img = 'arequipa.jpg'
    dest2.precio = 650

    dest3 = dest()
    dest3.nombre = 'Trujillo'
    dest3.descripcion = 'La ciudad de la eterna primavera'
    dest3.img = 'trujillo.jpg'
    dest3.precio = 725

    dest4 = dest()
    dest4.nombre = 'Cuzco'
    dest4.descripcion = 'La ciudad de la maravilla del mundo'
    dest4.img = 'cuzco.jpg'
    dest4.precio = 725

    dest5 = dest()
    dest5.nombre = 'Puno'
    dest5.descripcion = 'La ciudad nueva'
    dest5.img = 'puno.jpg'
    dest5.precio = 800



    
    

    dests = [dest1, dest2, dest3, dest4, dest5]

    return render(request,"Destinos_Turísticos/index.html", {'dests': dests})
