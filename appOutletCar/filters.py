import django_filters
from .models import Coche

class FiltroCoches(django_filters.FilterSet):

	class Meta:
		model = Coche
		fields= ('color', 'anyo')