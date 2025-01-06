from django import forms
from .models import Cliente, Endereco, Emprestimo, Servico, Despesa


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email']


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'cep', 'numero_residencia', 'bairro', 'cidade', 'estado']


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['id', 'idcliente', 'nomeBanco', 'nomeCorretor', 'produto', 'data_inicio_emprestimo',
                  'data_final_emprestimo', 'valorEmprestimo', 'status', 'comissaoCorretor', 'comissaoLLPromo']
        widgets = {
            'idcliente': forms.Select(attrs={'class': 'js-example-basic-single'}),
        }


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['id', 'idcliente', 'descricao', 'preco', 'data_servico']
        widgets = {
            'idcliente': forms.Select(attrs={'class': 'js-example-basic-single'}),
        }


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['id', 'idcliente', 'descricao', 'preco', 'data_despesa']
        widgets = {
            'idcliente': forms.Select(attrs={'class': 'js-example-basic-single'}),
        }

