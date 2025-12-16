from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from apps.listas.models import Lista
from .models import Tarefa, Tag # obs pessoal: o .arquivo se refere a um arquivo dentro do diretorio atual

@login_required(login_url='login')
def adicionar_tarefa(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id, usuario=request.user)
    
    if request.method == "POST":
        titulo_tarefa = request.POST.get('titulo_tarefa').strip()
        prazo_tarefa = request.POST.get('prazo') # Captura o prazo
        
        if titulo_tarefa:
            Tarefa.objects.create(
                nome=titulo_tarefa,
                usuario=request.user,
                lista=lista,
                concluido=False,
                prazo=prazo_tarefa if prazo_tarefa else None
            )
            
    return redirect('detalhe_lista', lista_id=lista_id)

@login_required(login_url='login')
def toggle_tarefa(request, lista_id, tarefa_id):
    tarefa = get_object_or_404(
        Tarefa, 
        pk=tarefa_id, 
        lista__pk=lista_id, 
        usuario=request.user
    )
    
    # alterna o valor: True vira False, e False vira True.
    tarefa.concluido = not tarefa.concluido
    tarefa.save()
    
    return redirect('detalhe_lista', lista_id=lista_id)

@login_required(login_url='login')
def apagar_tarefa(request, lista_id, tarefa_id):
    tarefa = get_object_or_404(
        Tarefa, 
        pk=tarefa_id, 
        lista__pk=lista_id, 
        usuario=request.user
    )
    
    tarefa.delete()

    return redirect('detalhe_lista', lista_id=lista_id)

@login_required(login_url='login')
def editar_tarefa(request, lista_id, tarefa_id):
    tarefa = get_object_or_404(
        Tarefa, 
        pk=tarefa_id, 
        lista__pk=lista_id, 
        usuario=request.user
    )
    
    if request.method == 'POST':
        if 'nome_tarefa' in request.POST:
            novo_nome = request.POST.get('nome_tarefa').strip()
            if novo_nome:
                tarefa.nome = novo_nome
                tarefa.save()
        
        elif 'prazo_tarefa' in request.POST:
            novo_prazo = request.POST.get('prazo_tarefa')
            
            if novo_prazo:
                tarefa.prazo = novo_prazo
            else:
                tarefa.prazo = None
                
            tarefa.save()

    return redirect('detalhe_lista', lista_id=lista_id)

@login_required(login_url='login')
def apagar_tarefas_concluidas(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id, usuario=request.user)
    
    Tarefa.objects.filter(lista=lista, concluido=True).delete()
    
    return redirect('detalhe_lista', lista_id=lista_id)

@login_required(login_url='login')
def gerenciar_tags(request):
    # busca todas as tags do usuário
    tags = Tag.objects.filter(usuario=request.user).order_by('nome')

    if request.method == 'POST':
        # se for para criar uma nova tag
        if 'criar_tag' in request.POST:
            nome_tag = request.POST.get('nome_tag').strip()
            if nome_tag:
                Tag.objects.get_or_create(
                    nome=nome_tag,
                    usuario=request.user
                )
        
        # se for para apagar uma tag
        elif 'apagar_tag_id' in request.POST:
            tag_id = request.POST.get('apagar_tag_id')
            Tag.objects.filter(pk=tag_id, usuario=request.user).delete()
            
        return redirect('gerenciar_tags')
        
    contexto = {
        'tags': tags
    }
    return render(request, 'tarefas/gerenciar_tags.html', contexto)
