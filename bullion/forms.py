from django import forms
from . import models


class BootstrapModelForm(forms.ModelForm):
    """Adds class 'form-control' to every field, for Bootstrap."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CoinModelForm(BootstrapModelForm):
    class Meta:
        model = models.Coin
        fields = '__all__'
