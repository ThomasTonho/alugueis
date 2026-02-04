
from django.urls import path
from .views import *

app_name = "api"

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('usuario/<int:pk>/', detalhar_usuario),
    path('imoveis/', listar_imoveis),
    path('imovel/<int:pk>/', detalhar_imovel),
    path('contratos/', listar_contratos),
    path('contrato/<int:pk>/', detalhar_contrato),
    path('pagamentos/', listar_pagamentos),
    path('pagamento/<int:pk>/', detalhar_pagamento),
]