from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return HttpResponse('Bienvenue sur mon blog')

def liste_articles(request):
    articles = [
        {'titre': 'Article 1', 'auteur': 'Michel', 'contenu': 'contenu de mon article 1'},
        {'titre': 'Article 2', 'auteur': 'Johnny', 'contenu': 'contenu de mon article 2'},
        {'titre': 'Article 3', 'auteur': 'René', 'contenu': 'contenu de mon article 3'},
    ]
    return render(request, 'liste_articles.html', {'articles': articles})

def contact(request):
    return render(request, 'contact.html')

def article_detail(request, pk):
    article = [
        {'titre': 'Article 1', 'auteur': 'Michel', 'contenu': 'contenu de mon article 1'},
        {'titre': 'Article 2', 'auteur': 'Johnny', 'contenu': 'contenu de mon article 2'},
        {'titre': 'Article 3', 'auteur': 'René', 'contenu': 'contenu de mon article 3'},
    ]

    return render(request, 'article_detail.html', {'article': article})

