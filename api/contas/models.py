from django.db import models

# Create your models here.
from django.db.models import Model


class Pagamento(models.Model):
    nome = models.CharField('Nome', max_length=100)
    valor_original = models.FloatField('Valor')
    valor_corrigido = models.FloatField('Valor', null=True, blank=True)
    vencimento = models.DateField('Data de Vencimento')
    pagamento = models.DateField('Data de Pagamento', auto_now_add=True)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Contas'

    def get_valor_corrigido(self):
        if self.pagamento <= self.vencimento:
            return self.valor_original
        else:
            diferenca_em_dias = (self.pagamento - self.vencimento).days
            if diferenca_em_dias <= 3:
                multa = self.valor_original * 0.02
                juros = self.valor_original * (diferenca_em_dias * 0.01)
            elif 3 < diferenca_em_dias <= 5:
                multa = self.valor_original * 0.03
                juros = self.valor_original * (diferenca_em_dias * 0.02)
            else:
                multa = self.valor_original * 0.05
                juros = self.valor_original * (diferenca_em_dias * 0.03)
            return self.valor_original + multa + juros

    def save(self, *args, **kwargs):
        self.valor_original = self.get_valor_corrigido()
        super(Pagamento, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome
