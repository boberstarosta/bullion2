from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, BaseUpdateView
from . import forms, models, stooq


class MetalListView(ListView):
    model = models.Metal
    context_object_name = 'all_metals'


class CoinListView(ListView):
    model = models.Coin
    context_object_name = 'all_coins'


class CoinDetailView(DetailView):
    model = models.Coin
    context_object_name = 'coin'


class CoinCreateView(CreateView):
    model = models.Coin
    form_class = forms.CoinModelForm


class CoinUpdateView(UpdateView):
    model = models.Coin
    form_class = forms.CoinModelForm


class CoinDeleteView(DeleteView):
    model = models.Coin
    success_url = reverse_lazy('coin_list')


class UpdateMetalPricesView(CreateView):
    def post(self, request):
        print('UpdateMetalPrices POST received')
        stooq.update_metal_prices()
        metals = models.Metal.objects.all()
        data = {}
        for metal in metals:
            last_price = metal.last_price
            data[metal.stooq_symbol] = {
                'pricePerOz': last_price.value_per_oz,
                'pricePerGram': last_price.value_per_gram,
            }
        return JsonResponse(data)
