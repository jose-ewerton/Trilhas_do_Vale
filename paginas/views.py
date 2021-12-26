from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from base.models import Categoria, Usuario, Local
from paginas.forms import UsuarioForm

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

@login_required(login_url='index')
def Locais(request):

    categorias = Categoria.objects.all()
    locais = Local.objects.all()
    busca = request.GET.get('busca')
    categorias_id = request.GET.get('categoria', None)

    if categorias_id is not None:    
        locais = Local.getLocaisByID(categorias_id)
        paginator = Paginator(locais, 6)

        page = request.GET.get('page')
        locais = paginator.get_page(page)

    elif busca:

        locais = Local.objects.filter(nome__icontains=busca)
        paginator = Paginator(locais, 6)

        page = request.GET.get('page')
        locais = paginator.get_page(page)

    else:
        categorias = Categoria.objects.all()
        locais = Local.objects.all()
        paginator = Paginator(locais, 6)

        page = request.GET.get('page')
        locais = paginator.get_page(page)
    return render(request,'paginas/locais.html', {'locais': locais, 'categorias': categorias})


    


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




def Login(request):
    if request.method=="POST":
      
        loginusuario=request.POST['loginusuario']
        loginsenha=request.POST['loginsenha']

        user=authenticate(username= loginusuario, password= loginsenha)
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Usuário/Senha inválido,tente novamente!")
            return redirect("index")

    return HttpResponse("login")

def Logout(request):
    logout(request)
    messages.success(request, "Deslogado")
    return redirect('index')
      