import requests
from bs4 import BeautifulSoup

from .article_data import SELECTORS


def extract_article_data(article):
    img_url = ""
    article_title = article.find('span', class_='main-news_super_item_title').text.strip()
    img_element = article.find('img', class_='main-news_top_item_img')
    time = article.find('time').text.strip()
    article_url = article.find('a')['href']
    if not article_url.startswith('https'):
        article_url = "https://tengrinews.kz/" + article_url
    if img_element:
        img_url = "https://tengrinews.kz/" + img_element['src']
    return {"title": article_title, "img_url": img_url, "date": time, "article_url" : article_url}


def extract_section_data(section):
    section_title = section.find('h2', class_='subhead-rubric').find('a').text.strip()
    current_article = []
    section_items = section.find_all_next('div', class_="main-news_top_item")

    for data in section_items:
        try:
            article_url = data.find('a')['href']
            if not article_url.startswith('https'):
                article_url = "https://tengrinews.kz/" + article_url

            img_url = ""
            img_element = data.find('img', class_='main-news_top_item_img')
            article_title = data.find('span', class_='main-news_top_item_title').find('a').text.strip()
            time = data.find('div', class_='main-news_top_item_meta').find('span').text.strip()
            if img_element:
                img_url = "https://tengrinews.kz/" + img_element['src']
            current_article.append({"title": article_title, "img_url": img_url, "date": time, "article_url" : article_url})
        except Exception as e:
            print("smth wrong:", e)
    return {"title": section_title, "article_data": current_article}


def scrape_tengri_news():
    url = 'https://tengrinews.kz/'
    response = requests.get(url)
    news = []
    section_data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        news_articles = soup.find_all('div', class_='main-news_super_item')
        news = [extract_article_data(article) for article in news_articles]

        sections = soup.find_all('section', class_='top-news')
        section_data = [extract_section_data(section) for section in sections]

    else:
        print("Ошибка при получении данных:", response.status_code)

    return news, section_data


def get_tengri_article(link, article_type):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        selectors = SELECTORS[article_type]

        title = soup.find(*selectors["title"]).text.strip()
        date = soup.find(*selectors["date"]).text.strip()
        description = [tag.text for tag in soup.find(*selectors["description"]).find_all("p")]
        image_url = "https://tengrinews.kz/" + soup.find(*selectors["image"]).find("img")["src"]
        tags = selectors["tags"]

        return {"title": title, "date": date, "description": description, "image_url": image_url, "tags": tags}
    else:
        raise Exception("Failed to fetch article data")