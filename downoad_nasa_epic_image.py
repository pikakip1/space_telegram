from photo_download import image_download
import argparse
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import urllib.parse


def fetch_nasa_epic_images(token, photos_number):
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    response = requests.get(url)
    response.raise_for_status()

    form_photo_url = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/epic_1b_{}.png{}'
    photo_urls = []
    api_key = {'api_key': token}

    for index, reply in enumerate(response.json(), 1):
        date = datetime.fromisoformat(reply['date']).strftime('%Y/%m/%d')
        photo_id = reply['identifier']
        params = f'?{urllib.parse.urlencode(api_key)}'

        photo_urls.append(form_photo_url.format(date, photo_id, params))
        if index == photos_number:
            return photo_urls


def set_argument():
    parser = argparse.ArgumentParser(description='''
        Программа скачивает определенное количество epic фотографий из nasa, на основе
        переданного аргумента.
        Аргумент --count_photo, отвечает за количество фото (по умолчанию 1). 
        Агумент --file_name, отвечает за имя директории(по умолчанию nasa_epic).
        Аргумент --photo_name, отвечает за название фото(по умолчанию epic)
    ''')

    parser.add_argument('-c', '--count_photo', default=3)
    parser.add_argument('-f', '--file_name', default='epic_nasa')
    parser.add_argument('-p', '--photo_name', default='epic')
    return parser.parse_args()


def main():
    args = set_argument()
    load_dotenv('TOKENS.env')
    token = os.environ['NASA_KEY']

    nasa_epic_urls = fetch_nasa_epic_images(token, args.count_photo)

    os.makedirs(args.file_name, exist_ok=True)
    number_photo = len(os.listdir(args.file_name))

    for nasa_epic_url in nasa_epic_urls:
        image_download(nasa_epic_url, args.file_name, args.photo_name, number_photo)
        number_photo += 1


if __name__ == '__main__':
    main()
