from django.db.models import fields
from app.models import Sponsor
from django.forms import ModelForm

class SponserForm(ModelForm):
    class Meta:
        model=Sponsor
        fields="__all__"
        