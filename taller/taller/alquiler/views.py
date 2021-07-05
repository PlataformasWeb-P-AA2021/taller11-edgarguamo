from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

from alquiler.models import * 
from alquiler.forms import * 

def index(request):
    """
    Mostrar toda la información en general 
    """
    edificio = Edificio.objects.all()
    departamento = Departamento.objects.all()
    inf_template = {'edificio': edificio, 'departamento':departamento}
    return render(request, 'index.html',inf_template)

"""
Metodos para Edificio
"""

def crear_edificio(request):
    if request.method=="POST":
        form = EdificioForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = EdificioForm()
    dic = {'form': form}
    return render(request, 'crearEdificio.html', dic)


def editar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)


def eliminar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

"""
Métodos Departamentos
"""
def crear_departamento (request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = DepartamentoForm()
    dic = {'form': form}
    return render(request, 'crearDepartamento.html', dic)


def editar_departamento(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarDepartamento.html', diccionario)


def eliminar_departamento(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

