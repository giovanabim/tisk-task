from django.urls import path
from . import views

urlpatterns = [
    path('listas/adicionar/', views.adicionar_lista, name = 'adicionar_lista'), # para o botao +
    path('listas/<int:lista_id>/', views.detalhe_lista, name = 'detalhe_lista'), # pagina da lista
    path('listas/<int:lista_id>/apagar/', views.apagar_lista, name = 'apagar_lista'),
]
