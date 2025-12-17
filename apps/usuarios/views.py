from django.shortcuts import render, redirect
from .forms import UsuarioForm, LoginForm # o formulario do user de cadastro e login
from .models import Usuario # o model do user

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from apps.listas.models import Lista
from apps.tarefas.models import Tarefa

def cadastrar_usuario(request):
    if request.method == "POST": # se o usuario enviar o formulario
        form = UsuarioForm(request.POST)
        if form.is_valid(): # checa se os campos estao preenchidos e validoos
            usuario = form.save(commit=False) # nao salva no banco de dados
            usuario.set_password(form.cleaned_data['senha']) # para salvar a senha com seguranca
            usuario.save() # salva o user
            return redirect('login') # mudar dps para home
    else: # se o request == "GET"
        form = UsuarioForm()

    return render(request, 'usuarios/cadastro.html', {'form': form}) # renderiza o template

def logar_usuario(request):
    if request.method == "POST": 
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            usuario = authenticate(request, username=email, password=senha)

            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                form.add_error(None, 'Email ou Senha inválidos. Tente novamente.')
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

@login_required(login_url='login')
def home(request):
    usuario_logado = request.user # contem o objeto Usuario logado
    listas = Lista.objects.filter(usuario=usuario_logado).prefetch_related('tarefa_set') # busca todas as listas do usuario logado e as tarefas contidas nelas
    
    prioridades_a_esconder = request.GET.getlist('esconder_prioridade')
    if prioridades_a_esconder:
        listas = listas.exclude(prioridade__in=prioridades_a_esconder)

    listas = listas.order_by('-prioridade')
    
    contexto = { # para o template
        'listas': listas,
        'prioridades_escondidas': prioridades_a_esconder,
    }
    return render(request, 'usuarios/home.html', contexto)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def apagar_conta(request):
    usuario = request.user
    usuario.delete() 
    return redirect('login')