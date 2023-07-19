import requests
import os
import re
from os.path import splitext


def get_extension(url):
    enlargement = splitext(url)[-1]

    if not (enlargement.strip('.')).isalpha():
        pattern = r'(\.[a-z]+)'
        enlargement = re.search(pattern, enlargement).group(0)
    return enlargement


def image_download(url, img_path, img_name):
    os.makedirs(img_path, exist_ok=True)
    response = requests.get(url)
    enlargement = get_extension(url)
    number_photo = len(os.listdir(img_path))

    with open(f'{img_path}/{img_name}{number_photo}{enlargement}', 'wb') as file:
        file.write(response.content)
