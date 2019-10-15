from django.urls import path
from . import views

urlpatterns = [
    path(r'django', views.show_django, name='index'),
    path('affichage', views.show_affichage, name='detail'),
    path('templates', views.show_templates, name='results'),
]
