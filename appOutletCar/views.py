from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Marca, Modelo, Coche, Usuario, Lugar
from .filters import FiltroCoches
from django.views.generic import ListView, DetailView



class ListViewCoches(ListView):
	model = Coche
	template_name = 'coche_lista.html'
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['filter']=SnippetFilter(self.request.GET, queryset=self.get_queryset())
		return context
class SnippetDetailView(DetailView):
    model = Coche
    template_name = 'coche_detalle.html'