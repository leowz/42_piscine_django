from django.urls import path, include

from . import views

urlpatterns = [
    path('populate/', views.populate),
    path('display/', views.display),
    path('remove/', views.remove),
]
