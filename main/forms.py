from django.forms import ModelForm
from main.models import TokoEntry
from django.utils.html import strip_tags

class TokoEntryForm(ModelForm):
    class Meta:
        model = TokoEntry
        fields = ["nama", "harga", "description", "image_url"]
    
    def clean_product(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)