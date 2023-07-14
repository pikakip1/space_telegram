from photo_download import image_download
import argparse
import requests
from datetime import datetime
from dotenv import load_dotenv
import os


def get_epic_image(token, photo_count):
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    response = requests.get(url)
    response.raise_for_status()
    photo_urls = []

    for index, reply in enumerate(response.json(), 1):
        date = datetime.fromisoformat(reply['date']).strftime('%Y/%m/%d')
        photo_id = reply['identifier']
        photo_urls.append([date, photo_id])
        if index == photo_count:
            break

    payload = {'api_key': token}

    urls = []
    for date, photo_id in photo_urls:
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/epic_1b_{photo_id}.png?api_key={token}'
        urls.append(url)
    return urls


def main():
    parser = argparse.ArgumentParser(description=
                                     '''Программа скачивает определенное количество epic фотографий из nasa, на основе
                                     переданного аргумента.\n
                                     Аргумент --count_photo, отвечает за количество фото (по умолчанию 1).\n
                                     Агумент --file_name, отвечает за имя директории(по умолчанию nasa_epic).\n
                                     Аргумент --photo_name, отвечает за название фото(по умолчанию epic)'''
                                     )
    parser.add_argument('-c', '--count_photo', default=3)
    parser.add_argument('-f', '--file_name', default='epic_nasa')
    parser.add_argument('-p', '--photo_name', default='epic')
    args = parser.parse_args()

    load_dotenv('NASA_TOKEN.env')
    token = os.environ['NASA_KEY']

    nasa_epic_urls = get_epic_image(token, args.count_photo)
    for nasa_epic_url in nasa_epic_urls:
        image_download(nasa_epic_url, args.file_name, args.photo_name)


if __name__ == '__main__':
    main()