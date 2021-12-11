from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from base.models import Usuario
from paginas.forms import UsuarioForm

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

def salva_cadastro(request):
    nome= request.POST.get('nome')
    email= request.POST.get('email')
    senha= request.POST.get('senha')
    count = Usuario.objects.filter(nome=nome, email=email).count()
    if count > 0:
        messages.error(request, 'Dados já existente, tente outro email ou usuário!')
        return redirect (reverse('index') + '#modalForm')
    else:
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect (reverse('index') + '#modalForm')


        