from django.urls import path
from . import views
urlpatterns = [  
	 path('', views.ListViewCoches.as_view(), name='list'),

    path('<int:pk>/', views.DetailViewCoches.as_view(), name='detail')
]
