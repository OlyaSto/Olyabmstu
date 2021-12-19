from .models import Rases, Cans
from django.forms import ModelForm, TextInput, Textarea


class RasesForm(ModelForm):
    class Meta:
        model = Rases
        fields = ['name', 'discription']

        widgets = {
            "name": TextInput(attrs = {
               'class': 'form-control',
                'placeholder' : 'Название расы'
            }),
            "discription": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),

        }

class CansForm(ModelForm):
    class Meta:
        model = Cans
        fields = ['idrases', 'cans']

        widgets = {
            "idrases": TextInput(attrs = {
               'class': 'form-control',
                'placeholder' : 'ID расы'
            }),
            "cans": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Способность'
            }),

        }