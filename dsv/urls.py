from django.urls import path
from .views import lista_processo, lista_equipamentos, atualizar_processo, atualizar_equipamentos, delete_processos, criar_processos, home, detalhes_processo, lista_equipamentos, atualizar_equipamentos, delete_equipamentos, criar_equipamentos, detalhes_equipamentos

urlpatterns = [
    path('lista_processos/', lista_processo, name="lista_processos"),
    path('update_processo/<int:id>', atualizar_processo, name="update_processo"),
    path('delete_processos/<int:id>', delete_processos, name="delete_processos"),
    path('criar_processos/', criar_processos, name="criar_processos"),
    path('detalhes_processo/<int:id>', detalhes_processo, name='detalhes_processo'),
    path('lista_equipamentos/<int:id>', lista_equipamentos, name="lista_equipamentos"),
    path('update_equipamentos/<int:id>', atualizar_equipamentos, name="update_equipamentos"),
    path('delete_equipamentos/<int:id>', delete_equipamentos, name="delete_equipamentos"),
    path('criar_equipamentos/', criar_equipamentos, name="criar_equipamento"),
    path('detalhes_equipamentos/<int:id>', detalhes_equipamentos, name='detalhes_equipamentos'),
    path('', home),
   
]