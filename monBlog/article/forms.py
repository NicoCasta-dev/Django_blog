from django import forms
from .models import Article
from django.forms import ModelForm

class Creer_Article_Form(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

class Supprimer_Article_Form(forms.Form):
    class Meta:
        model = Article
        fields = '__all__'