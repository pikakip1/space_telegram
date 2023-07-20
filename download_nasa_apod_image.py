import os
import requests
from photo_download import image_download
from dotenv import load_dotenv
import argparse


def fetch_nasa_apod_image(nasa_token, count=1):

    payload = {'api_key': nasa_token, 'count': count}
    url = f'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return [reply['hdurl'] for reply in response.json()]


def set_argument():
    parser = argparse.ArgumentParser(description='''
        Программа скачивает указанное количество фотографий дня, из api nasa.
        Аргумент photo_count, отвечает за количество фото(по умолчанию одно).
        Агумент --file_name, отвечает за имя директории(по умолчанию nasa_apod).
        Аргумент --photo_name, отвечает за название фото(по умолчанию apod)
    ''')

    parser.add_argument('-c', '--photo_count', default=1)
    parser.add_argument('-f', '--file_name', default='nasa_apod')
    parser.add_argument('-p', '--photo_name', default='apod')
    return parser.parse_args()


def main():
    args = set_argument()

    load_dotenv('TOKENS.env')
    nasa_token = os.environ['NASA_KEY']
    nasa_apod_urls = fetch_nasa_apod_image(nasa_token, args.photo_count)

    os.makedirs(args.file_name, exist_ok=True)
    number_photo = len(os.listdir(args.file_name))

    for nasa_apod_url in nasa_apod_urls:
        image_download(nasa_apod_url, args.file_name, args.photo_name, number_photo)
        number_photo += 1


if __name__ == '__main__':
    main()
