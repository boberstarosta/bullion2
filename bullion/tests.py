from django.test import TestCase
from .models import Metal, Price


class MetalModelTests(TestCase):
    def setUp(self):
        pass


class PriceModelTests(TestCase):
    def setUp(self):
        self.gold = Metal.objects.create(stooq_symbol='XAUPLN', name='Gold', short='Au')
        self.silver = Metal.objects.create(stooq_symbol='XAGPLN', name='Silver', short='Ag')

    def test_value_per_gram(self):
        price = Price(metal=self.gold, value=3110.0)
        self.assertEqual(price.value_per_gram, 100.0)
