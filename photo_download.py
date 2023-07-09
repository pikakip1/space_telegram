import requests
import os
import re
from os.path import splitext


def image_download(url, img_way, img_name):
    if not os.path.isdir(img_way):
        os.mkdir(img_way)

    files_count = len(os.listdir(img_way))

    for number, url in enumerate(url, files_count):
        response = requests.get(url)
        enlargement = splitext(url)[-1]

        if not (enlargement.strip('.')).isalpha():
            pattern = '(\.[a-z]+)'
            enlargement = re.search(pattern, enlargement).group(0)

        with open(f'{img_way}/{img_name}{number}{enlargement}', 'wb') as file:
            file.write(response.content)

