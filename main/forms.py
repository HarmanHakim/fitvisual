from django.forms import ModelForm
from main.models import TokoEntry

class TokoEntryForm(ModelForm):
    class Meta:
        model = TokoEntry
        fields = ["nama", "harga", "description"]