from django.urls import path, include
from . import views

app_name = 'appOutletCar'
urlpatterns = [  
	 path('', views.ListViewCoches.as_view(), name='list'),
    path('<int:pk>/', views.DetailViewCoches.as_view(), name='detail')
]
