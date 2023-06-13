from django import forms
from .models import Butaca

class ButacaForm(forms.ModelForm):
    class Meta:
        model = Butaca
        exclude = ['campo_no_deseado']