from photo_download import image_download
import requests
import argparse


def fetch_spacex_last_launch(fetch_id=''):
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(fetch_id)
    headers = {'Auth': 'False'}

    response_spacex = requests.get(url, headers=headers)
    response_spacex.raise_for_status()

    if fetch_id:
        fetch = response_spacex.json()['links']['flickr']['original']
        if fetch:
            return fetch
        print(f'В директории {fetch}, фото не обнаружено.\nЗагружаю последний запуск')

    for index in range(len(response_spacex.json()), 0, -1):
        try:
            last_fetch = response_spacex.json()[index]['links']['flickr']['original']
            if last_fetch:
                print(f'Загружен запуск {index}')
                return last_fetch
        except IndexError:
            continue


def main():
    parser = argparse.ArgumentParser(description=
                                    '''Программа скачивает все фото последнего запуска по умолчанию, если не был передан
                                    аргумент с директорией нужного запуска.\n
                                    Аргумент --fetch_id, отвечает за id полета(по умолчанию крайний полет).\n
                                    Агумент --file_name, отвечает за имя директории(по умолчанию spacex_launch).\n
                                    Аргумент --photo_name, отвечает за название фото(по умолчанию spacex)'''
                                    )
    parser.add_argument('-id', '--fetch_id', default='')
    parser.add_argument('-f', '--file_name', default='spacex_fetch')
    parser.add_argument('-p', '--photo_name', default='spacex')
    args = parser.parse_args()
    image_download(fetch_spacex_last_launch(args.fetch_id), args.file_name, args.photo_name)


if __name__ == '__main__':
    main()