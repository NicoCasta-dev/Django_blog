from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Creer_Article_Form, Creer_Auteur_Form, Supprimer_Article_Form
from .models import *


def liste_articles(request):
    articles = Article.objects.all
    return render(request, 'liste_articles.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(id = pk)
    return render(request, 'article_detail.html', {'article': article})


def creer_article(request):
    if request.method == 'POST':
        form = Creer_Article_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    
    return render(request, 'ajout.html', {'form': Creer_Article_Form, 'title': 'Créer un article'})

def ajouter_auteur(request):
    if request.method == "POST":
        form = Creer_Auteur_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("liste_articles")
        
    return render(request, 'ajouter_auteur.html', {'form': Creer_Auteur_Form, 'titre': 'Ajouter auteur'})
    

def supprimer_article(request, pk):
        article = Article.objects.get(id = pk)
        article.delete()
        return redirect('liste_articles')

def modifier_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == 'POST':
        form = Creer_Article_Form(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
        
    form = Creer_Article_Form(instance=article)
    return render(request, 'modifier_article.html', {'form':form})