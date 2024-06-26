from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .newsMainService import *
from .newsMainService.article_data import SELECTORS
from .newsMainService.news_main_service import *

def index(request):
    top_news, section_data = scrape_tengri_news()
    return render(request, "newsMain/mainPage.html", {"top_news": top_news, "section_data": section_data})


def current_article(request):
    link_received = request.GET.get('link')
    type = request.GET.get('type')
    if type not in SELECTORS:
        raise ValueError("Invalid article type")

    data = get_tengri_article(link_received, type)

    return render(request, "newsMain/articlePage.html", {"data": data})

