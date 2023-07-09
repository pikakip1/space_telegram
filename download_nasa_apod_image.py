import os
import requests
from photo_download import image_download
from dotenv import load_dotenv
import argparse


def nasa_apod_image(nasa_token, count=1):

    payload = {'api_key': nasa_token, 'count': count}
    url = f'https://api.nasa.gov/planetary/apod?'
    response = requests.get(url, params=payload)

    return [apod_json['hdurl'] for apod_json in response.json()]


def main():
    parser = argparse.ArgumentParser(description=
                                     '''Программа скачивает указанное количество фотографий дня, из api nasa.\n
                                     Аргумент photo_count, отвечает за количество фото(по умолчанию одно).\n
                                     Агумент --file_name, отвечает за имя директории(по умолчанию nasa_apod).\n
                                     Аргумент --photo_name, отвечает за название фото(по умолчанию apod)'''
                                     )
    parser.add_argument('-c', '--photo_count', default=1)
    parser.add_argument('-f', '--file_name', default='nasa_apod')
    parser.add_argument('-p', '--photo_name', default='apod')
    args = parser.parse_args()

    load_dotenv('NASA_TOKEN.env')
    nasa_token = os.environ['NASA_KEY']
    image_download(nasa_apod_image(nasa_token, args.photo_count), args.file_name, args.photo_name)


if __name__ == '__main__':
    main()

