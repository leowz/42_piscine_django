"""d07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from ex00.views import HomeView, ArticlesView
# from ex01.views import PublicationsView, ArticleDetailView, FavoritesView
# from ex02.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
     # ex00
	path('', HomeView.as_view(), name='home'),
	path('articles/', ArticlesView.as_view(template_name = 'articles.html'), name="articles"),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	#ex01
	# path('publications/', PublicationsView.as_view(template_name = 'ex01/publications.html'), name='publications'),
	# path('detail/(?P<pk>[0-9]+)/', ArticleDetailView.as_view(template_name = "ex01/detail.html"), name="detail"),
	# path('logout/', auth_views.LogoutView.as_view(template_name='ex01/logout.html'), name='logout'),
	# path('favorites/', FavoritesView.as_view(template_name='ex01/favorites.html'), name="favorites"),
	#ex02
	# url(r'^register/$', RegisterView.as_view(template_name='ex02/register.html'), name="register"),
]
