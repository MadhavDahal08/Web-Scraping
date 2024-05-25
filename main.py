import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movies_list = [movie.getText() for movie in movies]
movies_list.reverse()

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for item in movies_list:
        file.write(item+'\n')
