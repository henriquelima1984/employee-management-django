from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView
from django.views.generic.edit import UpdateView
from employee_management.models import Funcionario
from website.forms import InsereFuncionarioForm


class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionario"


class FuncionarioUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")

    def get_object(self, queryset=None):
        funcionario = None

        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            funcionario = Funcionario.objetos.filter(id=id).first()

        elif slug is not None:
            campo_slug = self.get_slug_field()

            funcionario = Funcionario.objetos.filter(**{campo_slug: slug}).first()

        return funcionario


class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")


class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionario")
