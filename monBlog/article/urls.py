from django.urls import path
from . import views

urlpatterns = [
    path ('articles/', views.liste_articles, name='liste_articles'),
    path ('<int:pk>/', views.article_detail, name='article_detail'),
    path ('creer_article/', views.creer_article, name='creer_article'),
    path ('supprimer_article/', views.supprimer_article, name='supprimer_article'),
    ]

