
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]