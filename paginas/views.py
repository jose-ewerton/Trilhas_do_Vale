from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from base.models import Categoria, Local


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
        paginator = Paginator(locais, 10)

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
    if request.method=="GET":
        return render (request, 'paginas/index.html')
    else:
        nome= request.POST.get('nome')
        email= request.POST.get('email')
        senha= request.POST.get('senha')

        user = User.objects.filter(email=email).count()
        if user > 0:
            messages.error(request, 'Dados já existente, tente outro email!')
            return redirect (reverse('index') + '#modalForm')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Cadastrado com sucesso!')
            return redirect (reverse('index') + '#modalForm')




def Login(request):
    if request.method=="GET":
           return render (request, 'paginas/index.html')
    else:
        loginusuario = request.POST['loginusuario']
        loginsenha = request.POST['loginsenha']

        user = authenticate(username=loginusuario, password=loginsenha)
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Usuário/Senha inválido,tente novamente!")
            return redirect("index")

def Logout(request):
    logout(request)
    messages.success(request, "Deslogado")
    return redirect('index')
      