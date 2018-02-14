from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


GRAMS_PER_OZ = 31.1


class Metal(models.Model):
    stooq_symbol = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='nazwa')
    short = models.CharField(max_length=10, verbose_name='skrót')

    class Meta:
        verbose_name = 'Metal'
        verbose_name_plural = 'Metale'

    @property
    def last_price(self):
        return Price.last_price(self)

    def __str__(self):
        return self.name


class Price(models.Model):
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE, verbose_name='metal')
    time = models.DateTimeField(auto_now_add=True, verbose_name='czas')
    value_per_oz = models.FloatField(verbose_name='wartość 1 oz')

    class Meta:
        verbose_name = 'Cena'
        verbose_name_plural = 'Ceny'

    @property
    def value_per_gram(self):
        # noinspection PyTypeChecker
        return self.value_per_oz / GRAMS_PER_OZ

    @classmethod
    def last_price(cls, metal):
        return cls.objects.filter(metal=metal).order_by('-time').first()

    def __str__(self):
        return '{} {} {}'.format(self.metal, self.time.strftime('%Y-%m-%d %H:%M:%S'), self.value_per_oz)


class Coin(models.Model):
    country = models.CharField(max_length=100, verbose_name='państwo')
    face_value = models.CharField(max_length=100, verbose_name='nominał')
    mint_years = models.CharField(max_length=100, verbose_name='lata wydania')
    description = models.CharField(max_length=200, blank=True, default='', verbose_name='opis')

    metal = models.ForeignKey(Metal, on_delete=models.CASCADE, verbose_name='metal')
    weight = models.FloatField(validators=[MinValueValidator(0.01)], verbose_name='waga [g]')
    fineness = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(1000)],
                                   verbose_name='próba [/1000]')

    class Meta:
        verbose_name = 'Moneta'
        verbose_name_plural = 'Monety'

    def inline_text(self):
        fields = [self.country, self.face_value, self.mint_years, self.description]
        return ' '.join(str(f) for f in fields)

    @property
    def pure_weight(self):
        return self.weight * self.fineness / 1000

    @property
    def last_price(self):
        metal_price = self.metal
        if metal_price is None:
            return None
        else:
            return self.pure_weight * metal_price.value_per_gram

    def get_absolute_url(self):
        return reverse('coin_detail', kwargs={'pk': self.pk})

    def __str__(self):
        fields = [self.country, self.face_value, self.mint_years]
        return ', '.join(str(x) for x in fields)
