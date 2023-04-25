from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome_cliente', 'contatos_cliente', 'tipo_cliente', 'cpf_cnpj', 'data_nascimento_criacao']