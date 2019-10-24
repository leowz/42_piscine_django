from django.shortcuts import HttpResponse, render, redirect
from ex00.models import Article, UserFavoriteArticle
from django.views.generic import TemplateView, ListView, FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

class HomeView(TemplateView):
    model = Article

    def get(self, request):
    	if (request.user.is_authenticated):
    		return redirect(reverse('articles'))
    	else:
    		return redirect(reverse('login'))

class ArticlesView(ListView):
    model = Article
    template_name = "article.html"