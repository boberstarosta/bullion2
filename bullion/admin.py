from django.contrib import admin
from . import models


admin.site.register(models.Metal)
admin.site.register(models.Coin)
admin.site.register(models.Price)
