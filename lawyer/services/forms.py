from django.forms import ModelForm
#from django.forms.widgets import Textarea
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = {'first_name', 'last_name', 'phone'}
