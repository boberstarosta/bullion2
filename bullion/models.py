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

    def __str__(self):
        return self.name


class Price(models.Model):
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE, verbose_name='metal')
    time = models.DateTimeField(auto_now_add=True, verbose_name='czas')
    value = models.FloatField(verbose_name='wartość')

    class Meta:
        verbose_name = 'Cena'
        verbose_name_plural = 'Ceny'

    @property
    def value_per_gram(self):
        # noinspection PyTypeChecker
        return self.value / GRAMS_PER_OZ

    @classmethod
    def last_value_per_gram(cls, metal):
        return cls.objects.order_by('-time').first().value_per_gram

    def __str__(self):
        return '{} {} {}'.format(self.metal, self.time.strftime('%Y-%m-%d %H:%M:%S'), self.value)


class Coin(models.Model):
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE)
    weight = models.FloatField(validators=[MinValueValidator(0.01)], verbose_name='waga [g]')
    fineness = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(1000)],
                                   verbose_name='próba [/1000]')
    country = models.CharField(max_length=100, verbose_name='państwo')
    face_value = models.CharField(max_length=100, verbose_name='nominał')
    mint_years = models.CharField(max_length=100, verbose_name='lata wydania')
    description = models.CharField(max_length=200, blank=True, default='', verbose_name='opis')

    class Meta:
        verbose_name = 'Moneta'
        verbose_name_plural = 'Monety'

    def inline_text(self):
        fields = [self.country, self.face_value, self.mint_years, self.description]
        return ' '.join(str(f) for f in fields)

    def get_absolute_url(self):
        return reverse('coin_detail', kwargs={'pk': self.pk})

    def __str__(self):
        fields = [self.country, self.face_value, self.mint_years]
        return ', '.join(str(x) for x in fields)
