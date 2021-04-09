from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser

from contas.serializers import PagamentoSerializer
from rest_framework.permissions import AllowAny


class PagamentoCreate(CreateAPIView):
    """
        Cadastra um pagamento. Clique em Try Out para cadastrar por aqui.
    """
    serializer_class = PagamentoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]