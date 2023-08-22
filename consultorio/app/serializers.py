from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'idade', 'endereco', 'bairro', 'cep', 'cidade', 'uf', 'genero']