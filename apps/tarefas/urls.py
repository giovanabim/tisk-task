from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('<int:tarefa_id>/toggle/', views.toggle_tarefa, name='toggle_tarefa'),
    path('<int:tarefa_id>/apagar/', views.apagar_tarefa, name='apagar_tarefa'),
    path('apagar_concluidas/', views.apagar_tarefas_concluidas, name='apagar_tarefas_concluidas'),
    # nome e prazo
    path('<int:tarefa_id>/editar/', views.editar_tarefa, name='editar_tarefa'), 
]