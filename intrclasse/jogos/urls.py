from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'jogos'
urlpatterns = [
    path('', views.index, name='index'),
    path('equipes/<int:pk>/', views.equipe, name='equipe'),
    path('modalidades/<int:pk>/', views.modalidade, name='modalidade'),
]
