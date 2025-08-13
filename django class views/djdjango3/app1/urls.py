from django.urls import path
from . import views


urlpatterns = [
    path('', views.pozdrav_meno, name='pozdrav'),
    path('kategoria/', views.vyber_kategoriu, name='vyber-kategorie'),

]