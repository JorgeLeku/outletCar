from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.

from django.http import HttpResponse
from .models import Marca, Modelo, Coche, Usuario, Lugar
from .filters import FiltroCoches
from django.views.generic import ListView, DetailView



class ListViewCoches(ListView):
	model = Coche
	template_name = 'coche_lista.html'


class SnippetDetailView(DetailView):
    model = Coche
    template_name = 'coche_detalle.html'