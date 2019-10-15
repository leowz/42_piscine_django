from django.shortcuts import render
from django.http import HttpResponse

def show_django(request):
    return render(request, 'django.html', { 'title': "ex01: django"});

def show_affichage(request):
    return render(request, 'affichage.html', { 'title': "ex01: affichage"});

def show_templates(request):
    return render(request, 'templates.html', { 'title': "ex01: templates"});


