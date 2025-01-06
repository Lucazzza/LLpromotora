from django.contrib import admin
from .models import Cliente, Emprestimo, Servico, Despesa, Endereco


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email')
    search_fields = ('nome', 'telefone', 'email')


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_cliente_nome', 'logradouro', 'cep', 'numero_residencia', 'bairro', 'cidade', 'estado')
    search_fields = ('logradouro', 'cep', 'numero_residencia', 'bairro', 'cidade', 'estado')

    def get_cliente_nome(self, obj):
        return obj.cliente.nome
    get_cliente_nome.short_description = 'Cliente'


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_cliente_nome', 'nomeBanco', 'nomeCorretor', 'produto',
                    'data_inicio_emprestimo', 'data_final_emprestimo',
                    'valorEmprestimo', 'status', 'comissaoCorretor', 'comissaoLLPromo')
    list_filter = ('idcliente__nome', 'status')
    search_fields = ('nomeBanco', 'status', 'idcliente__nome')

    def get_cliente_nome(self, obj):
        return obj.idcliente.nome
    get_cliente_nome.short_description = 'Cliente'


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_cliente_nome', 'descricao', 'preco', 'data_servico')
    search_fields = ('user__username', 'descricao')

    def get_cliente_nome(self, obj):
        return obj.idcliente.nome
    get_cliente_nome.short_description = 'Cliente'


class DespesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_cliente_nome', 'descricao', 'preco', 'data_despesa')
    search_fields = ('user__username', 'descricao')

    def get_cliente_nome(self, obj):
        return obj.idcliente.nome
    get_cliente_nome.short_description = 'Cliente'


# Registrar os modelos com as classes ModelAdmin personalizadas
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Despesa, DespesaAdmin)
