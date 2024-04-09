import requests
from bs4 import BeautifulSoup


class News:
    title = ""
    image_url = ""
    creating_date = ""
    category = ""

    def __init__(self, title, image_url, creating_date):
        self.title = title
        self.image_url = image_url
        self.creating_date = creating_date


import requests
from bs4 import BeautifulSoup


def extract_article_data(article):
    img_url = ""
    article_title = article.find('span', class_='main-news_super_item_title').text.strip()
    img_element = article.find('img', class_='main-news_top_item_img')
    time = article.find('time').text.strip()
    article_url = "https://tengrinews.kz/" + article.find('a')["href"]
    if img_element:
        img_url = "https://tengrinews.kz/" + img_element['src']
    return {"title": article_title, "img_url": img_url, "date": time, "article_url" : article_url}


def extract_section_data(section):
    section_title = section.find('h2', class_='subhead-rubric').find('a').text.strip()
    current_article = []
    section_items = section.find_all_next('div', class_="main-news_top_item")

    for data in section_items:
        try:
            article_url = "https://tengrinews.kz/" + data.find('a')['href']

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


def get_tengri_article(link):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        date = soup.find('div', class_="date-time").text.strip()
        title = soup.find("h1", class_="head-single").text.strip()
        description = soup.find("div", class_='content_main_text').text.strip()
        image_url = "https://tengrinews.kz/" + soup.find("picture", class_='content_main_thumb_img').find("img")["src"]
        tags_container = soup.find("div", class_="content_main_text_tags")
        tags = [tag.text.strip() for tag in tags_container.find_all("span")]

        return {"title" : title, "date" : date, "description" : description, "image_url" : image_url, "tags": tags}


def get_tengri_life_article(link):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("h1", class_="post-title").text.strip()
        date = soup.find("span", class_="date")
        description = [tag.text for tag in soup.find("div", class_="post-content").find_all("p")]

