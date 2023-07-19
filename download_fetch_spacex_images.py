from photo_download import image_download
import requests
import argparse


def fetch_spacex_last_launch(launch_id):
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)

    spacex_response = requests.get(url)
    spacex_response.raise_for_status()
    launch_information = spacex_response.json()

    if not isinstance(launch_information, list):
        launch_information = [launch_information]

    for i in reversed(launch_information):
        photo_launch = i['links']['flickr']['original']
        if photo_launch:
            print(f'Был загружен запуск {i["id"]}')
            return photo_launch


def main():
    parser = argparse.ArgumentParser(argument_default='5eb87ce7ffd86e000604b33b', description='''
        Программа скачивает все фото последнего запуска по умолчанию, если не был передан
        аргумент с директорией нужного запуска.\n
        Аргумент --launch_id, отвечает за id полета(по умолчанию крайний полет).\n
        Агумент --file_name, отвечает за имя директории(по умолчанию spacex_launch).\n
        Аргумент --photo_name, отвечает за название фото(по умолчанию spacex)
    ''')

    parser.add_argument('-id', '--launch_id')
    parser.add_argument('-f', '--file_name', default='spacex_fetch')
    parser.add_argument('-p', '--photo_name', default='spacex')
    args = parser.parse_args()

    spacex_urls = fetch_spacex_last_launch(args.launch_id)
    for spacex_url in spacex_urls:
        image_download(spacex_url, args.file_name, args.photo_name)


if __name__ == '__main__':
    main()
