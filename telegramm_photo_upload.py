import os
import random
import argparse
from dotenv import load_dotenv
import telegram


def telegramm_photo_post(token, chat_id, directory, photo_name):
    bot = telegram.Bot(token=token)

    if photo_name is None:
        photo_name = ''.join(random.choices(os.listdir(directory)))

    with open(f'{directory}/{photo_name}', 'rb') as photo:
        bot.send_document(chat_id=chat_id, document=photo)


def main():
    parse = argparse.ArgumentParser(description='''
        Скрипт позволяет выборочно постить изображение в чат.
        Если фото не выбрано, скрипт отправлят случайное фото из файла.
        Требует два обязательных аргумента: id чата(id_chat) и папку с фото(directory).
    ''')

    parse.add_argument('-id', '--id_chat', default='@cosmo_photos')
    parse.add_argument('-d', '--directory', default='nasa_apod')
    parse.add_argument('-p', '--photo_name', default=None)

    args = parse.parse_args()

    load_dotenv('TOKENS.env')
    token = os.environ['TELEGRAMM_KEY']

    telegramm_photo_post(token, args.id_chat, args.directory, args.photo_name)


if __name__ == '__main__':
    main()
    