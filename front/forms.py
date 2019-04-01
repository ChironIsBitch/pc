from django.forms import ModelForm
from . import models


class CarForm(ModelForm):
    class Meta:
        model = models.Start
        fields = ('start_choices', 'end_choices', 'start_time', 'beizhu')