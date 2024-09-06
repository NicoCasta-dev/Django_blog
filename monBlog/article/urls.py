from django.urls import path
from . import views

urlpatterns = [
    path ('articles/', views.liste_articles, name='liste_articles'),
    path ('<int:pk>/', views.article_detail, name='article_detail'),
    path ('creer_article/', views.creer_article, name='creer_article'),
    path ('ajouter_auteur/', views.ajouter_auteur, name='ajouter_auteur'),
    path ('supprimer/<int:pk>/', views.supprimer_article, name='supprimer_article'),
    path ('modifier_article/<int:pk>', views.modifier_article, name='modifier_article')
    ]

