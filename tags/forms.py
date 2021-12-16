from django.forms import ModelForm

from tags.models import Tags


class RegisterTagForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = "Имя"
