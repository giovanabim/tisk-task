from django.urls import path, include
from . import views

urlpatterns = [
    path('listas/adicionar/', views.adicionar_lista, name='adicionar_lista'), 
    path('listas/<int:lista_id>/detalhe/', views.detalhe_lista, name='detalhe_lista'), 
    path('listas/<int:lista_id>/apagar/', views.apagar_lista, name='apagar_lista'),

    path('listas/<int:lista_id>/', include('apps.tarefas.urls')),
]