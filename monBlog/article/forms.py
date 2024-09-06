from django import forms
from .models import Article, Author
from django.forms import ModelForm

class Creer_Article_Form(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

class Creer_Auteur_Form(forms.Form):
    class Meta:
        model = Author
        fields = '__all__'

class Supprimer_Article_Form(forms.Form):
    class Meta:
        model = Article
        fields = '__all__'