from django.forms import ModelForm
from django import forms
from status.models import Status


class RegisterStatusesForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Имя'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
