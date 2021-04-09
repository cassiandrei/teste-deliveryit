from django.urls import path

from core.views import index

from contas.views import PagamentoCreate

app_name = 'contas'
urlpatterns = [
    path('pagamento/', PagamentoCreate.as_view()),
]
