import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

rescourse = requests.get(url=URL)
website = rescourse.text

soup = BeautifulSoup(website, "html.parser")
movies = soup.find_all(name="h3", class_="title")
# numbers_rank = [int(movie.getText().split()[0]) for movie in movies]
movies_rank = [movie.getText() for movie in movies]
# print(numbers_rank)
# movies_rank.reverse()
# for ranking in movies_rank:
#     print(ranking)
with open("movies.txt", mode="w") as file:
    for movie in movies_rank[::-1]:
        file.write(f"{movie}\n")
