from django import forms

from .models import Worker

class AddWorker(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"