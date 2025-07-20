from django import forms
from django.forms import ModelForm
from .models import Fest, Anmeld 

class FestForm(forms.ModelForm):
  name = forms.CharField(
    widget= forms.TextInput(
    attrs={'placeholder': 'ny forespørgsel...'}))

  class Meta:
      model = Fest
      fields = '__all__'

class AnmeldForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'ny anmeldelse...'}))

  class Meta:
    model = Anmeld 
    fields = '__all__'