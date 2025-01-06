from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome Completo')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(max_length=254, verbose_name='E-mail')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    cep = models.CharField(max_length=10, verbose_name='CEP')
    numero_residencia = models.CharField(max_length=10, verbose_name='Número')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    class Meta:
        db_table = 'endereco'

    def __str__(self):
        return self.cidade


class Emprestimo(models.Model):
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nomeBanco = models.CharField(max_length=20, verbose_name='Nome do Banco')
    nomeCorretor = models.CharField(max_length=20, verbose_name='Nome do Corretor')
    produto = models.CharField(max_length=20, verbose_name='Modelo de Empréstimo')
    data_inicio_emprestimo = models.DateField(verbose_name='Data Inicio do Emprestimo')
    data_final_emprestimo = models.DateField(verbose_name='Data Fim do Emprestimo')
    valorEmprestimo = models.CharField(max_length=20, verbose_name='Total do Empréstimo')
    status = models.CharField(max_length=20, verbose_name='Status')
    comissaoCorretor = models.CharField(max_length=20, verbose_name='Comissão Corretor')
    comissaoLLPromo = models.CharField(max_length=20, verbose_name='Comissão LLPROMOTORA')

    class Meta:
        db_table = 'emprestimo'

    def __str__(self):
        return self.nomeBanco


class Servico(models.Model):
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=20, verbose_name='Nome do Serviço')
    preco = models.CharField(max_length=20, verbose_name='Valor do Cobrado')
    data_servico = models.DateField(verbose_name='Data do Serviço')

    class Meta:
        db_table = 'servico'

    def __str__(self):
        return self.descricao


class Despesa(models.Model):
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=20, verbose_name='Nome da Despesa')
    preco = models.CharField(max_length=20, verbose_name='Valor do Cobrado')
    data_despesa = models.DateField(verbose_name='Data da Despesa')

    class Meta:
        db_table = 'despesa'

    def __str__(self):
        return self.descricao
