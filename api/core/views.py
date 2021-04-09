from django.shortcuts import render, redirect

from contas.models import Pagamento


def index(request):
    pagamentos = Pagamento.objects.all()
    context = {
        'pagamentos': pagamentos
    }
    return render(request, 'core/index.html', context=context)
