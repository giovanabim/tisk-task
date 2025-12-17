from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lista
from apps.tarefas.models import Tag, Tarefa
from django.db.models import F

@login_required(login_url='login')
def adicionar_lista(request):
    lista = Lista.objects.create(
        usuario = request.user,
        nome = "Nova Lista Sem Nome",
    )
    return redirect('detalhe_lista', lista_id = lista.pk)

@login_required(login_url='login')
def detalhe_lista(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id, usuario=request.user) # segurança

    if request.method == 'POST': # ações de edição
        if 'nome_lista' in request.POST: # input
            novo_nome = request.POST.get('nome_lista').strip() # salva o valor do input
            if novo_nome: # checa se está vazio
                lista.nome = novo_nome
                lista.save()
        
        if 'prioridade_lista' in request.POST:
            nova_prioridade = request.POST.get('prioridade_lista')
            if nova_prioridade in ['alta', 'media', 'baixa']:
                lista.prioridade = nova_prioridade
                lista.save()
        
        return redirect('detalhe_lista', lista_id = lista.pk)
    tarefas = lista.tarefa_set.all().order_by('concluido', 
                                              F('prazo').asc(nulls_last=True),
                                              'id')

    tags_filtradas_ids = request.GET.getlist('filtro_tag')
    if tags_filtradas_ids:
        tarefas = tarefas.filter(tags__in = tags_filtradas_ids).distinct()

    tags_disponiveis = Tag.objects.filter(usuario=request.user).order_by('nome')

    contexto = {
        'lista': lista,
        'tarefas': tarefas,
        'tags': tags_disponiveis,
        'tags_filtradas_ids': tags_filtradas_ids,
    }

    return render(request, 'listas/detalhes.html', contexto)

@login_required(login_url='login')
def apagar_lista(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id, usuario=request.user)
    lista.delete()
    return redirect('home')
