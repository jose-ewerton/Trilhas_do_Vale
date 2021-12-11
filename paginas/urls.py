from django.urls import path
from .views import PaginaInicial, salva_cadastro

urlpatterns = [
path('', PaginaInicial.as_view(), name='index'),
#path('endereco/',MinhaView.as_view(),nome)
path('salva_cadastro', salva_cadastro, name='salva_cadastro'),
]