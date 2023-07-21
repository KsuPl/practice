import requests
from bs4 import BeautifulSoup

base_url = input(
    'Введите ссылку на исполнителя на Яндекс. Музыка, '
    'например, https://music.yandex.ru/artist/117334/tracks: ')
try:
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "lxml")
    songs = soup.find_all("div", class_="d-track__name")
    artists = soup.find_all("h1",
                            class_="page-artist__title typo-h1 typo-h1_big")
    print(f"10 самых популярных треков исполнителя "
          f"{artists[0].text.strip()}: ")
    # print(soup)
    for i in range(10):
        print(f"{i + 1}. {songs[i].text.strip()}")
except requests.exceptions.MissingSchema:
    print('Нет сссылки')
except requests.exceptions.InvalidSchema:
    print('Нет адаптера подключения')
