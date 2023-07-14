from photo_download import image_download
import requests
import argparse


def fetch_spacex_last_launch(launch_id):
    if launch_id is None:
        launch_id = ''
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)
    headers = {'Auth': 'False'}

    spacex_response = requests.get(url, headers=headers)
    spacex_response.raise_for_status()

    if launch_id:
        fetch = spacex_response.json()['links']['flickr']['original']
        if fetch:
            return fetch
        print(f'В директории {fetch}, фото не обнаружено.\nЗагружаю последний запуск')

    for index in range(len(spacex_response.json()), 0, -1):
        try:
            last_fetch = spacex_response.json()[index]['links']['flickr']['original']
            if last_fetch:
                print(f'Загружен запуск {index}')
                return last_fetch
        except IndexError:
            continue


def main():
    parser = argparse.ArgumentParser(description=
                                    '''Программа скачивает все фото последнего запуска по умолчанию, если не был передан
                                    аргумент с директорией нужного запуска.\n
                                    Аргумент --launch_id, отвечает за id полета(по умолчанию крайний полет).\n
                                    Агумент --file_name, отвечает за имя директории(по умолчанию spacex_launch).\n
                                    Аргумент --photo_name, отвечает за название фото(по умолчанию spacex)'''
                                    )
    parser.add_argument('-id', '--launch_id')
    parser.add_argument('-f', '--file_name', default='spacex_fetch')
    parser.add_argument('-p', '--photo_name', default='spacex')
    args = parser.parse_args()

    spacex_urls = fetch_spacex_last_launch(args.launch_id)
    for spacex_url in spacex_urls:
        image_download(spacex_url, args.file_name, args.photo_name)


if __name__ == '__main__':
    main()