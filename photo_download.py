import requests
import os
import re
from os.path import splitext


def create_folder(img_way):
    os.makedirs(img_way, exist_ok=True)


def count_photo(img_way):
    return len(os.listdir(img_way))


def get_extension(url):
    enlargement = splitext(url)[-1]

    if not (enlargement.strip('.')).isalpha():
        pattern = '(\.[a-z]+)'
        enlargement = re.search(pattern, enlargement).group(0)
    return enlargement


def image_download(url, img_way, img_name):
    create_folder(img_way)
    response = requests.get(url)
    enlargement = get_extension(url)
    number_photo = count_photo(img_way)

    with open(f'{img_way}/{img_name}{number_photo}{enlargement}', 'wb') as file:
        file.write(response.content)


