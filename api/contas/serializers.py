from rest_framework import serializers

from contas.models import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):
    """
     Pagamento
    """

    class Meta:
        model = Pagamento
        fields = ['nome', 'valor_original', 'vencimento', 'pagamento']
