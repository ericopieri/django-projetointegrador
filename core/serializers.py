from dataclasses import field
from django.contrib.auth.hashers import make_password

from rest_framework.serializers import ModelSerializer
from core.models import (
    Usuario,
    Endereco,
    Cartao,
    Cor,
    Tamanho,
    Marca,
    Produto,
    Pedido,
    Avaliacao,
    Forma_Pagamento,
    Ped_Pro,
)


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def validate_password(self, value: str) -> str:
        return make_password(value)


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class CartaoSerializer(ModelSerializer):
    class Meta:
        model = Cartao
        fields = "__all__"


class Forma_PagamentoSerializer(ModelSerializer):
    class Meta:
        model = Forma_Pagamento
        fields = "__all__"


class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"


class TamanhoSerializer(ModelSerializer):
    class Meta:
        model = Tamanho
        fields = "__all__"


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class Ped_ProSerializer(ModelSerializer):
    class Meta:
        model = Ped_Pro
        fields = "__all__"


class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
