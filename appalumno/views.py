from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('pagina inicial la mama de todas')
def mi_alumno(request):
    return HttpResponse('<h1>Hola alumno feo<h1>')
def mi_alumna(request):
    return HttpResponse('<h1>Es Una alumna seria<h1>')