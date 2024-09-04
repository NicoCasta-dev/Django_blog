from django.urls import path, include
from . import views

app_name = 'article'

urlpatterns = [
    path ('', views.accueil, name='accueil'),
    path ('articles/', views.liste_articles, name='liste_articles'),
    path ('<int:pk>/', views.article_detail, name='article_detail'),
    path ('contact/', views.contact, name='contact'),
    ]

