import requests
from bs4 import BeautifulSoup as bs

best_movies = []
all_films = []


def parsing_all_movies():
    global all_films
    for i in range(1, 10):
        url = f"https://kinogo.uk/page/{i}/"
        data_from_the_site = requests.get(url)
        soup = bs(data_from_the_site.text, "html.parser")
        films = soup.findAll('div', class_='line-clamp')
        for film in films:
            all_films.append(film.text.strip())
            
def parsing_the_best():
    global best_movies
    for i in range(1, 10):
        url = f"https://kinogo.uk/top/movie/top_rated/page/{i}"
        data_from_the_site = requests.get(url)
        soup = bs(data_from_the_site.text, "html.parser")
        films = soup.findAll('div', class_='short_title')
        for film in films:
            best_movies.append(film.text.strip())
            