from django.forms import ModelForm
from django import forms
from labels.models import Labels


class RegisterTagForm(ModelForm):
    class Meta:
        model = Labels
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Имя'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = "Имя"
