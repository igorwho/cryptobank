from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def list_clientes(request):
    return HttpResponse("Lista de clientes: 001, 002")