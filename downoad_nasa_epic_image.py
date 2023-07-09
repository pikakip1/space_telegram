from photo_download import image_download
import argparse
import requests
from datetime import datetime
from dotenv import load_dotenv
import os


def get_epic_image(token, photo_count):
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    response = requests.get(url)
    photo_url = []

    for index, file_json in enumerate(response.json(), 1):
        date = datetime.fromisoformat(file_json['date']).strftime('%Y/%m/%d')
        photo_id = file_json['identifier']
        photo_url.append([date, photo_id])
        if index == photo_count:
            break

    payload = {'api_key': token}

    urls = []
    for data, photo_id in photo_url:
        url = f'https://api.nasa.gov/EPIC/archive/natural/{data}/png/epic_1b_{photo_id}.png'

        response = requests.get(url, params=payload)
        urls.append(response.url)
    return urls


def main():
    parser = argparse.ArgumentParser(description=
                                     '''Программа скачивает определенное количество epic фотографий из nasa, на основе
                                     переданного аргумента.\n
                                     Аргумент --count_photo, отвечает за количество фото (по умолчанию 1).\n
                                     Агумент --file_name, отвечает за имя директории(по умолчанию nasa_epic).\n
                                     Аргумент --photo_name, отвечает за название фото(по умолчанию epic)'''
                                     )
    parser.add_argument('-c', '--count_photo', default=1)
    parser.add_argument('-f', '--file_name', default='spacex_fetch')
    parser.add_argument('-p', '--photo_name', default='spacex')
    args = parser.parse_args()

    load_dotenv('NASA_TOKEN.env')
    token = os.environ['NASA_KEY']
    image_download(get_epic_image(token, args.count_photo), args.file_name, args.photo_name)


if __name__ == '__main__':
    main()