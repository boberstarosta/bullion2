import time
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

    def test_last_value_per_gram(self):
        for value in range(5000, -1000, -1000):
            Price.objects.create(metal=self.gold, value=value)
            time.sleep(0.1)

        self.assertEqual(Price.last_value_per_gram(self.gold), 0)
