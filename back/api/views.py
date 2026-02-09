from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from rest_framework.decorators import api_view
from .serializers import (
    UsuarioSerializer, 
    ImovelSerializer, 
    ContratoSerializer, 
    PagamentoSerializer
    )

# GET E POST para Usuarios
@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':  
        queryset = Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':  
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, DELETE para Usuarios
@api_view(['GET', 'PUT', 'DELETE'])
def detalhar_usuario(request, pk):
    if request.method == 'GET':  
        usuario = Usuario.objects.get(pk=pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    elif request.method == 'PUT':  
        usuario = Usuario.objects.get(pk=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':  
        usuario = Usuario.objects.get(pk=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# GET E POST para Imoveis
@api_view(['GET','POST'])
def listar_imoveis(request):
    if request.method == 'GET':  
        queryset = Imovel.objects.all()
        serializer = ImovelSerializer(queryset, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':  
        serializer = ImovelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET, PUT, DELETE para Imoveis
@api_view(['GET', 'PUT', 'DELETE'])
def detalhar_imovel(request, pk):
    if request.method == 'GET':  
        imovel = Imovel.objects.get(pk=pk)
        serializer = ImovelSerializer(imovel)
        return Response(serializer.data)
    elif request.method == 'PUT':  
        imovel = Imovel.objects.get(pk=pk)
        serializer = ImovelSerializer(imovel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':  
        imovel = Imovel.objects.get(pk=pk)
        imovel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# GET E POST para Contratos
@api_view(['GET','POST'])
def listar_contratos(request):
    if request.method == 'GET':  
        queryset = Contrato.objects.all()
        serializer = ContratoSerializer(queryset, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':  
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET, PUT, DELETE para Contratos
@api_view(['GET', 'PUT', 'DELETE'])
def detalhar_contrato(request, pk):
    if request.method == 'GET':  
        contrato = Contrato.objects.get(pk=pk)
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)
    elif request.method == 'PUT':  
        contrato = Contrato.objects.get(pk=pk)
        serializer = ContratoSerializer(contrato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':  
        contrato = Contrato.objects.get(pk=pk)
        contrato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# GET E POST para Pagamentos
@api_view(['GET','POST'])
def listar_pagamentos(request):
    if request.method == 'GET':  
        queryset = Pagamento.objects.all()
        serializer = PagamentoSerializer(queryset, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':  
        serializer = PagamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET, PUT, DELETE para Pagamentos
@api_view(['GET', 'PUT', 'DELETE'])
def detalhar_pagamento(request, pk):
    if request.method == 'GET':  
        pagamento = Pagamento.objects.get(pk=pk)
        serializer = PagamentoSerializer(pagamento)
        return Response(serializer.data)
    elif request.method == 'PUT':  
        pagamento = Pagamento.objects.get(pk=pk)
        serializer = PagamentoSerializer(pagamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':  
        pagamento = Pagamento.objects.get(pk=pk)
        pagamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    