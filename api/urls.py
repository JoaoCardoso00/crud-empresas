from django.urls import path
from . import views

urlpatterns = [
    path('', views.getEmpresas),
    path('empresa/<int:pk>', views.getEmpresa),
    path('empresa/create', views.createEmpresa),
    path('empresa/<int:pk>/update', views.updateEmpresa),
    path('empresa/<int:pk>/delete', views.deleteEmpresa),
]
