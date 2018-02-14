import time
from django.test import TestCase
from .models import Coin, Metal, Price


class MetalModelTests(TestCase):
    def setUp(self):
        self.gold = Metal.objects.create(stooq_symbol='XAUPLN', name='Gold', short='Au')

    def test_last_price_per_oz_empty(self):
        self.assertIsNone(self.gold.last_price_per_oz)

    def test_last_price_per_oz(self):
        for value in range(0, 4000, 1000):
            Price.objects.create(metal=self.gold, value=value)
            time.sleep(0.1)
        self.assertEqual(self.gold.last_price_per_oz, 3000)

    def test_last_price_per_gram_empty(self):
        self.assertIsNone(self.gold.last_price_per_gram)

    def test_last_price_per_gram(self):
        for value in range(110, 4000, 1000):
            Price.objects.create(metal=self.gold, value=value)
            time.sleep(0.1)
        self.assertEqual(self.gold.last_price_per_gram, 100)


class PriceModelTests(TestCase):
    def setUp(self):
        self.gold = Metal.objects.create(stooq_symbol='XAUPLN', name='Gold', short='Au')
        self.silver = Metal.objects.create(stooq_symbol='XAGPLN', name='Silver', short='Ag')

    def test_value_per_gram(self):
        price = Price.objects.create(metal=self.gold, value=3110.0)
        self.assertEqual(price.value_per_gram, 100.0)

    def test_last_value_per_oz_empty(self):
        for value in range(5000, 0, -1000):
            Price.objects.create(metal=self.gold, value=value)
            time.sleep(0.1)
        Price.objects.create(metal=self.silver, value=10000.0)
        self.assertEqual(Price.last_value_per_oz(self.gold), 1000.0)

    def test_last_value_per_gram_empty(self):
        self.assertIsNone(Price.last_value_per_gram(self.gold))

    def test_last_value_per_gram(self):
        for value in range(5000, -1000, -1000):
            Price.objects.create(metal=self.gold, value=value)
            time.sleep(0.1)
        Price.objects.create(metal=self.silver, value=10000.0)

        self.assertEqual(Price.last_value_per_gram(self.gold), 0)


class CoinModelTests(TestCase):
    def setUp(self):
        self.gold = Metal.objects.create(stooq_symbol='XAUPLN', name='Gold', short='Au')

    def test_last_price(self):
        coin = Coin.objects.create(country='Cntr1', face_value='1fv', mint_years='2000', metal=self.gold, weight=20.0,
                                   fineness=500)

        self.assertIsNone(coin.last_price)

        for value in range(110, 4000, 1000):
            Price.objects.create(metal=self.gold, value=value)
            time.sleep(0.1)

        self.assertEqual(coin.last_price, 1000.0)
