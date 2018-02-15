from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView
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


class UpdateMetalPricesView(View):
    def post(self, request):
        stooq.update_metal_prices()
        data = models.Metal.last_prices_json()
        return JsonResponse(data)


class GetMetalPricesView(View):
    def get(self, request):
        data = models.Metal.last_prices_json()
        return JsonResponse(data)


class UpdateCoinPricesView(View):
    def post(self, request):
        stooq.update_metal_prices()
        data = models.Coin.last_prices_json()
        return JsonResponse(data)


class GetCoinPricesView(View):
    def get(self, request):
        data = models.Coin.last_prices_json()
        return JsonResponse(data)
