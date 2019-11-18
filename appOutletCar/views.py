from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Marca, Modelo, Coche, Usuario, Lugar, Comment
from .filters import FiltroCoches
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm

class ListViewCoches(ListView):
	model = Coche
	template_name = 'coche_lista.html'
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['filter']=FiltroCoches(self.request.GET, queryset=self.get_queryset())
		return context
class DetailViewCoches(DetailView):
    model = Coche
    template_name = 'coche_detalle.html'

def DetailViewCoches(request, slug):
    template_name = 'coche_detalle.html'
    coche = get_object_or_404(Coche, slug=slug)
    comments = coche.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'COCHE':
        comment_form = CommentForm(data=request.COCHE)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current coche to the comment
            new_comment.coche = coche
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'coche': coche,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
