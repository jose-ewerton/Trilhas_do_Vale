from django.urls import path
from .views import PaginaInicial, salva_cadastro, Locais
from . import views
urlpatterns = [
path('', PaginaInicial.as_view(), name='index'),
#path('endereco/',MinhaView.as_view(),nome)
path('salva_cadastro', salva_cadastro, name='salva_cadastro'),
path('locais/', views.Locais, name='locais'),
path('login', views.Login, name="Login"),
path('logout', views.Logout, name="Logout"),
]