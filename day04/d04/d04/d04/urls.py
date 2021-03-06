"""d04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ex00.views import render_index
from ex02.views import render_form
from ex03.views import show_table

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ex00/?$', render_index),
    url(r'^ex01/?', include('ex01.urls')),
    url(r'^ex02/?', render_form),
    url(r'^ex03/?', show_table),
]
