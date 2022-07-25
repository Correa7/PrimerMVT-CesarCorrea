from django.shortcuts import render
from django.http import HttpResponse
import datetime
from App1.models import Personas
from django.template import loader


def Pariente(self,vinculo, nombre, apellido, edad):
    
    pariente = Personas(vinculo=vinculo, nombre= nombre, apellido=apellido, edad=edad, fecha=datetime.datetime.now())
    pariente.save()
    
    return HttpResponse(f""" 
         <p>Familiar: {pariente.vinculo},
         Nombre: {pariente.nombre} {pariente.apellido}, 
         edad: {pariente.edad} años.
        Registro tomado el : {pariente.fecha}
         </p>
         """)

def lista_familiares(request):

    lista = Personas.objects.all()

    return render(request, "template.html",{"lista_familiares":lista})



