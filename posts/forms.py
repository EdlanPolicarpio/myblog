from django.forms import ModelForm
from . import models

class EntryForm(ModelForm):
    class Meta:
        model = models.Entry
        fields = ['title','body','slug','published']

