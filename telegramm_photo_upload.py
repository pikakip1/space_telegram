import os
import random
import argparse
from dotenv import load_dotenv
import telegram


def telegramm_photo_post(token, chat_id, directory, path):
    bot = telegram.Bot(token=token)
    if path:
        name_photo = os.listdir(directory)[path]
    else:
        name_photo = random.choices(os.listdir(directory))[0]

    with open(f'{directory}/{name_photo}', 'rb') as photo:
        bot.send_document(chat_id=chat_id, document=photo)


def main():
    parse = argparse.ArgumentParser(description='''
    Скрипт позволяет выборочно постить изображение в чат.
    Если фото не выбрано, скрипт отправлят случайное фото из файла.
    Требует два обязательных аргумента: id чата(id_chat) и папку с фото(directory).
    ''')

    parse.add_argument('id_chat')
    parse.add_argument('directory')
    parse.add_argument('-p', '--path', default=None)

    args = parse.parse_args()

    load_dotenv('TELEGRAMM_TOKEN.env')
    token = os.environ['TELEGRAMM_KEY']
    if args.directory is None:
        args.directory = 'nasa_apod'

    telegramm_photo_post(token, args.id_chat, args.directory, args.path)


if __name__ == '__main__':
    main()
    