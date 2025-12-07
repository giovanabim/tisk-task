from django.shortcuts import render, redirect
from .forms import UsuarioForm # o formulario do user
from .models import Usuario # o model do user

def cadastrar_usuario(request):
    if request.method == "POST": # se o usuario enviar o formulario
        form = UsuarioForm(request.POST)
        if form.is_valid(): # checa se os campos estao preenchidos e validoos
            usuario = form.save(commit=False) # nao salva no banco de dados
            usuario.senha = make_password(form.cleaned_data['senha']) # para salvar a senha com seguranca
            usuario.save() # salva o user
            return redirect('login') # mudar dps para home
    else: # se o request == "GET"
        form = UsuarioForm()

    return render(request, 'usuarios/cadastro.html', {'form': form}) # renderiza o template