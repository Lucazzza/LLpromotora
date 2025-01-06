from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .forms import ClienteForm, EnderecoForm, EmprestimoForm, ServicoForm, DespesaForm
from .models import Cliente, Emprestimo, Servico, Despesa
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q  # Importar Q para consultas complexas


# @login_required(login_url='login/teste')
# @never_cache
# def cliente_autocomplete(request):
#     if 'term' in request.GET:
#         # Filtrar clientes baseando-se no usuário autenticado
#         qs = Cliente.objects.filter(nome__icontains=request.GET.get('term'), user=request.user)
#         clientes = list(qs.values('id', 'nome'))
#         return JsonResponse(clientes, safe=False)
#     return JsonResponse([], safe=False)
#
#
# @login_required(login_url='login/teste')
# @never_cache
# def login_teste_view(request):
#     # Your view logic here
#     return render(request, 'teste.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            messages.warning(request, 'Usuário já cadastrado!')
            return redirect('login')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect(bemvindo)
        else:
            messages.warning(request, 'Usuário Inválido!')
            return redirect('login')


# @login_required(login_url='login/bemvindo')
# @never_cache
# def bemvindo(request):
#     emprestimos = Emprestimo.objects.filter(idcliente__user=request.user).order_by('id')
#     paginator = Paginator(emprestimos, 10)  # Mostra até 10 empréstimos por página
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'bemvindo.html', {'page_obj': page_obj})




@login_required(login_url='login/bemvindo')
@never_cache
def bemvindo(request):
    # Pegando os parâmetros do filtro
    cliente = request.GET.get('cliente')
    banco = request.GET.get('banco')
    corretor = request.GET.get('corretor')
    modelo = request.GET.get('modelo')
    data = request.GET.get('data')
    status = request.GET.get('status')

    # Pegando os parâmetros do filtro serviço
    servico_cliente = request.GET.get('servico_cliente')
    servico_descricao = request.GET.get('servico_descricao')
    servico_data_servico = request.GET.get('servico_data_servico')

    # Pegando os parâmetros do filtro despesa
    despesa_cliente = request.GET.get('despesa_cliente')
    despesa_descricao = request.GET.get('despesa_descricao')
    despesa_data_despesa = request.GET.get('despesa_data_despesa')

    # Filtrando os empréstimos com base no usuário e nos parâmetros de filtro
    emprestimos = Emprestimo.objects.filter(idcliente__user=request.user).order_by('id')

    # Filtrando os serviços com base no usuário e nos parâmetros de filtro
    servicos = Servico.objects.filter(idcliente__user=request.user).order_by('id')

    # Filtrando as despesas com base no usuário e nos parâmetros de filtro
    despesas = Despesa.objects.filter(idcliente__user=request.user).order_by('id')

    # Aplicando filtros adicionais para empréstimos
    if cliente:
        emprestimos = emprestimos.filter(idcliente__nome__icontains=cliente)
    if banco:
        emprestimos = emprestimos.filter(nomeBanco__icontains=banco)
    if corretor:
        emprestimos = emprestimos.filter(nomeCorretor__icontains=corretor)
    if modelo:
        emprestimos = emprestimos.filter(produto__icontains=modelo)
    if data:
        emprestimos = emprestimos.filter(data_inicio_emprestimo__icontains=data)
    if status:
        emprestimos = emprestimos.filter(status__icontains=status)

    # Aplicando filtros adicionais para serviços
    if servico_cliente:
        servicos = servicos.filter(idcliente__nome__icontains=servico_cliente)
    if servico_descricao:
        servicos = servicos.filter(descricao__icontains=servico_descricao)
    if servico_data_servico:
        servicos = servicos.filter(data_servico__icontains=servico_data_servico)

    # Aplicando filtros adicionais para despesas
    if despesa_cliente:
        despesas = despesas.filter(idcliente__nome__icontains=despesa_cliente)
    if despesa_descricao:
        despesas = despesas.filter(descricao__icontains=despesa_descricao)
    if despesa_data_despesa:
        despesas = despesas.filter(data_despesa__icontains=despesa_data_despesa)

    # Paginação para empréstimos
    paginator = Paginator(emprestimos, 10)  # Mostra até 10 empréstimos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Paginação para serviços
    servico_paginator = Paginator(servicos, 10)  # Mostra até 10 serviços por página
    servico_page_number = request.GET.get('servico_page')
    servico_page_obj = servico_paginator.get_page(servico_page_number)

    # Paginação para despesas
    despesa_paginator = Paginator(despesas, 10)  # Mostra até 10 despesas por página
    despesa_page_number = request.GET.get('despesa_page')
    despesa_page_obj = despesa_paginator.get_page(despesa_page_number)

    # Renderizando a página com os dados filtrados e paginados
    return render(request, 'bemvindo.html', {
        'page_obj': page_obj,
        'servico_page_obj': servico_page_obj,
        'despesa_page_obj': despesa_page_obj
    })


@login_required(login_url='login')
def logout_view(request):
    logout_django(request)
    return redirect('login')


@login_required(login_url='login/bemvindo')
def registrar_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        endereco_form = EnderecoForm(request.POST)

        if cliente_form.is_valid() and endereco_form.is_valid():
            cliente = cliente_form.save(commit=False)
            cliente.user = request.user
            cliente.save()

            endereco = endereco_form.save(commit=False)
            endereco.cliente = cliente
            endereco.save()

            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect(bemvindo)
        else:
            messages.error(request, "Erro ao cadastrar, verifique os dados!")
    else:
        cliente_form = ClienteForm()
        endereco_form = EnderecoForm()

    return render(request, 'bemvindo.html', {'cliente_form': cliente_form, 'endereco_form': endereco_form})


@login_required(login_url='login/bemvindo')
@never_cache
def cliente_autocomplete(request):
    if 'term' in request.GET:
        # Filtrar clientes baseando-se no usuário autenticado
        qs = Cliente.objects.filter(nome__icontains=request.GET.get('term'), user=request.user)
        clientes = list(qs.values('id', 'nome'))
        return JsonResponse(clientes, safe=False)
    return JsonResponse([], safe=False)


@login_required(login_url='login/bemvindo')
@never_cache
def registrar_emprestimo(request):
    if request.method == 'POST':
        emprestimo_form = EmprestimoForm(request.POST)

        if emprestimo_form.is_valid():
            emprestimo = emprestimo_form.save(commit=False)
            emprestimo.user = request.user
            emprestimo.save()

            messages.success(request, "Emprestimo cadastrado com sucesso!")
            return redirect(bemvindo)
        else:
            messages.error(request, "Erro ao cadastrar, verifique os dados!")

    else:
        emprestimo_form = EmprestimoForm()

    return render(request, 'bemvindo.html', {'emprestimo_form': emprestimo_form})


@login_required(login_url='login/bemvindo')
@never_cache
def registrar_servico(request):
    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)

        if servico_form.is_valid():
            servico = servico_form.save(commit=False)
            servico.user = request.user
            servico.save()

            messages.success(request, "Serviço cadastrado com sucesso!")
            return redirect(bemvindo)
        else:
            messages.error(request, "Erro ao cadastrar, verifique os dados!")

    else:
        servico_form = ServicoForm()

    return render(request, 'bemvindo.html', {'servico_form': servico_form})


@login_required(login_url='login/bemvindo')
@never_cache
def registrar_despesa(request):
    if request.method == 'POST':
        despesa_form = DespesaForm(request.POST)

        if despesa_form.is_valid():
            despesa = despesa_form.save(commit=False)
            despesa.user = request.user
            despesa.save()

            messages.success(request, "Despesa cadastrado com sucesso!")
            return redirect(bemvindo)
        else:
            messages.error(request, "Erro ao cadastrar, verifique os dados!")

    else:
        despesa_form = DespesaForm()

    return render(request, 'bemvindo.html', {'despesa_form': despesa_form})


@login_required(login_url='login/bemvindo')
@never_cache
def emprestimo_update(request):
    if request.method == 'POST':
        emprestimo_id = request.POST.get('emprestimoId')
        print(f"ID do Empréstimo Recebido: {emprestimo_id}")  # Adicione este print para depuração
        emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            print("Formulário é válido e salvo com sucesso.")  # Adicione este print para depuração
            return redirect(bemvindo)
        else:
            print(f"Formulário inválido: {form.errors}")  # Adicione este print para depuração
    return redirect(bemvindo)


@login_required(login_url='login/bemvindo')
@never_cache
def emprestimo_detail(request, id):
    emprestimo = Emprestimo.objects.get(id=id)
    data = {
        "id": emprestimo.id,
        "idcliente": emprestimo.idcliente.id,
        "nomecliente": emprestimo.idcliente.nome,
        "nomeBanco": emprestimo.nomeBanco,
        "nomeCorretor": emprestimo.nomeCorretor,
        "produto": emprestimo.produto,
        "data_inicio_emprestimo": emprestimo.data_inicio_emprestimo.strftime('%Y-%m-%d'),
        "data_final_emprestimo": emprestimo.data_final_emprestimo.strftime('%Y-%m-%d'),
        "valorEmprestimo": emprestimo.valorEmprestimo,
        "status": emprestimo.status,
        "comissaoCorretor": emprestimo.comissaoCorretor,
        "comissaoLLPromo": emprestimo.comissaoLLPromo,
    }
    return JsonResponse(data)



@login_required(login_url='login/bemvindo')
@never_cache
def emprestimo_delete(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)

    if request.method == 'POST':
        emprestimo.delete()
        return redirect(bemvindo)
    return redirect(bemvindo)


@login_required(login_url='login/bemvindo')
@never_cache
def servico_update(request):
    if request.method == 'POST':
        servico_id = request.POST.get('servicoId')
        print(f"ID do Serviço Recebido: {servico_id}")  # Adicione este print para depuração
        servico = get_object_or_404(Servico, id=servico_id)
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            print("Formulário é válido e salvo com sucesso.")  # Adicione este print para depuração
            return redirect(bemvindo)
        else:
            print(f"Formulário inválido: {form.errors}")  # Adicione este print para depuração
    return redirect(bemvindo)


@login_required(login_url='login/bemvindo')
@never_cache
def servico_detail(request, id):
    servico = Servico.objects.get(id=id)
    data = {
        "id": servico.id,
        "idcliente": servico.idcliente.id,
        "nomecliente": servico.idcliente.nome,
        "descricao": servico.descricao,
        "preco": servico.preco,
        "data_servico": servico.data_servico.strftime('%Y-%m-%d'),
    }
    return JsonResponse(data)


@login_required(login_url='login/bemvindo')
@never_cache
def servico_delete(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        servico.delete()
        return redirect(bemvindo)
    return redirect(bemvindo)


@login_required(login_url='login/bemvindo')
@never_cache
def despesa_update(request):
    if request.method == 'POST':
        despesa_id = request.POST.get('despesaId')
        print(f"ID do Serviço Recebido: {despesa_id}")  # Adicione este print para depuração
        despesa = get_object_or_404(Despesa, id=despesa_id)
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            print("Formulário é válido e salvo com sucesso.")  # Adicione este print para depuração
            return redirect(bemvindo)
        else:
            print(f"Formulário inválido: {form.errors}")  # Adicione este print para depuração
    return redirect(bemvindo)


@login_required(login_url='login/bemvindo')
@never_cache
def despesa_detail(request, id):
    despesa = Despesa.objects.get(id=id)
    data = {
        "id": despesa.id,
        "idcliente": despesa.idcliente.id,
        "nomecliente": despesa.idcliente.nome,
        "descricao": despesa.descricao,
        "preco": despesa.preco,
        "data_despesa": despesa.data_despesa.strftime('%Y-%m-%d'),
    }
    return JsonResponse(data)


@login_required(login_url='login/bemvindo')
@never_cache
def despesa_delete(request, id):
    despesa = get_object_or_404(Despesa, id=id)

    if request.method == 'POST':
        despesa.delete()
        return redirect(bemvindo)
    return redirect(bemvindo)