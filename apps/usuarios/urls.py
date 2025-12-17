from django.urls import path
from apps.tarefas import views as tarefas_views
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('login/', views.logar_usuario, name='login'),
    path('', views.home, name='home'),
    path('tags/gerenciar/', tarefas_views.gerenciar_tags, name='gerenciar_tags'),
    path('logout/', views.logout_view, name='logout'),
    path('apagar-conta/', views.apagar_conta, name='apagar_conta'),
]
