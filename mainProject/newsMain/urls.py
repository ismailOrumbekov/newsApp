from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainPage'),
    path('article', views.current_article, name='article')
]