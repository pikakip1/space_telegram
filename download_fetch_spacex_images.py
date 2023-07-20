from photo_download import image_download
import requests
import argparse
import os


def fetch_spacex_last_launch(launch_id):
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)

    spacex_response = requests.get(url)
    spacex_response.raise_for_status()
    launch_information = spacex_response.json()

    try:
        return launch_information['links']['flickr']['original']

    except TypeError:
        for reply in reversed(launch_information):
            photo_launch = reply['links']['flickr']['original']
            if photo_launch:
                print(f'Был загружен крайний запуск: {reply["id"]}')
                return photo_launch


def set_args():
    parser = argparse.ArgumentParser(description='''
        Программа скачивает все фото последнего запуска по умолчанию, если не был передан
        аргумент с директорией нужного запуска.\n
        Аргумент --launch_id, отвечает за id полета(по умолчанию крайний полет).\n
        Агумент --file_name, отвечает за имя директории(по умолчанию spacex_launch).\n
        Аргумент --photo_name, отвечает за название фото(по умолчанию spacex)
    ''')

    parser.add_argument('-id', '--launch_id', default='')
    parser.add_argument('-f', '--file_name', default='spacex_fetch')
    parser.add_argument('-p', '--photo_name', default='spacex')
    return parser.parse_args()


def main():
    args = set_args()
    spacex_urls = fetch_spacex_last_launch(args.launch_id)

    os.makedirs(args.file_name, exist_ok=True)
    number_photo = len(os.listdir(args.file_name))

    for spacex_url in spacex_urls:
        image_download(spacex_url, args.file_name, args.photo_name, number_photo)
        number_photo += 1


if __name__ == '__main__':
    main()
