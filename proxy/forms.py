from django.forms import ModelForm
from .models import Ipinfo

class IpForm(ModelForm):
    class Meta:
        model = Ipinfo
        fields = ['ip']