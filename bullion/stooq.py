import datetime
import re
import requests
from bs4 import BeautifulSoup
from bullion.models import Metal, Price
from django.conf import settings
from django.utils import timezone


def get_stooq_price(name):
    name = name.lower()
    url = 'https://stooq.pl/q/?s=' + name
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    search_phrase = 'aq_{name}_c[0-9]'.format(name=name)
    tag = soup.find('span', id=re.compile(search_phrase))
    if tag is None:
        return None
    else:
        try:
            return float(tag.get_text())
        except ValueError:
            return None


def update_metal_prices():
    for metal in Metal.objects.all():
        proceed = False
        last_price = metal.last_price
        if last_price is None:
            proceed = True
        else:
            now = timezone.now()
            last = metal.last_price.time
            max_interval = datetime.timedelta(seconds=settings.PRICE_MIN_UPDATE_INTERVAL)
            if now - last > max_interval:
                proceed = True
        if proceed:
            stooq_price = get_stooq_price(metal.stooq_symbol)
            if stooq_price is not None:
                Price.objects.create(metal=metal, value_per_oz=stooq_price)
