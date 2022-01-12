from django.forms import ModelForm
from status.models import Status
from django.utils.translation import gettext as _


class RegisterStatusesForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = _("Name")
