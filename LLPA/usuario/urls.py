from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login'), name='página inicial'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/bemvindo', views.bemvindo, name='login_bemvindo'),
    path('logout/', views.logout_view, name='logout'),
    path('bemvindo/cadastro_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('cliente-autocomplete/', views.cliente_autocomplete, name='cliente-autocomplete'),
    path('bemvindo/cadastro_emprestimo', views.registrar_emprestimo, name='registrar_emprestimo'),
    path('bemvindo/cadastro_servico', views.registrar_servico, name='registrar_servico'),
    path('bemvindo/cadastro_despesa', views.registrar_despesa, name='registrar_despesa'),
    path('bemvindo/emprestimo/update/', views.emprestimo_update, name='emprestimo_update'),  # Sem ID para POST
    path('bemvindo/emprestimo/detail/<int:id>/', views.emprestimo_detail, name='emprestimo_detail'),
    path('bemvindo/emprestimo/<int:id>/delete/', views.emprestimo_delete, name='emprestimo_delete'),
    path('bemvindo/servico/update/', views.servico_update, name='servico_update'),  # Sem ID para POST
    path('bemvindo/servico/detail/<int:id>/', views.servico_detail, name='servico_detail'),
    path('bemvindo/servico/<int:id>/delete/', views.servico_delete, name='servico_delete'),
    path('bemvindo/despesa/update/', views.despesa_update, name='despesa_update'),  # Sem ID para POST
    path('bemvindo/despesa/detail/<int:id>/', views.despesa_detail, name='despesa_detail'),
    path('bemvindo/despesa/<int:id>/delete/', views.despesa_delete, name='despesa_delete'),
]

