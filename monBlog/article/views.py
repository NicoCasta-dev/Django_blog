from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Creer_Article_Form, Supprimer_Article_Form
from . import models


def liste_articles(request):
    articles = models.Article.objects.all
    return render(request, 'liste_articles.html', {'articles': articles})

def article_detail(request, pk):
    article = models.Article.objects.get(id = pk)

    return render(request, 'article_detail.html', {'article': article})

def creer_article(request):
    if request.method == 'POST':
        form = Creer_Article_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    
    return render(request, 'ajout.html', {'form': Creer_Article_Form, 'title': 'Créer un article'})

def supprimer_article(request):
    form = Supprimer_Article_Form

    if request.method == 'GET':
        return render(request, 'supprimer.html', {'form': form})
    
    # if request.method == 'POST':
    