import requests
from bs4 import BeautifulSoup

target = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(target)
response.raise_for_status()
movie_page = response.text
soup = BeautifulSoup(movie_page, 'html.parser')
movie_titles = soup.find_all('img')
for title in movie_titles:
    print(title['alt'])
