from django.urls import path, include
from . import views
from outletCar import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'appOutletCar'
urlpatterns = [  
	path('', views.ListViewCoches.as_view(), name='list'),
    path('<slug:slug>/', views.DetailViewCoches, name='detail')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
