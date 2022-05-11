# Importamos a função index() definida no arquivo views.py
from django.urls import path
from website.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioDeleteView, \
    FuncionarioCreateView

app_name = 'website'

# Contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name='index'),
    path('funcionario/', FuncionarioListView.as_view(), name='lista_funcionario'),
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
]
