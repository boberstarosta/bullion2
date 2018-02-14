from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, BaseUpdateView
from . import forms, models


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
        data = {'text': 'I am a JsonResponse from django'}
        return JsonResponse(data)
