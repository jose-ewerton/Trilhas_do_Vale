from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from base.models import Categoria, Usuario, Local
from paginas.forms import UsuarioForm

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

def Locais(request):

    busca = request.GET.get('busca')
   
    if busca:

        locais = Local.objects.filter(nome__icontains=busca)

    else:
        
        locais = Local.objects.all()
        allcategorias = Categoria.objects.all()

    data = {
        'categorias': allcategorias,
        'locais': locais
    }
    return render(request,'paginas/locais.html', data) 

def salva_cadastro(request):
    nome= request.POST.get('nome')
    email= request.POST.get('email')
    senha= request.POST.get('senha')
    count = Usuario.objects.filter(email=email).count()
    if count > 0:
        messages.error(request, 'Dados já existente, tente outro email ou usuário!')
        return redirect (reverse('index') + '#modalForm')
    else:
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso!')
        return redirect (reverse('index') + '#modalForm')


        