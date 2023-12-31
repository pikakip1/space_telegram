import os
import random
import argparse
from dotenv import load_dotenv
from time import sleep
import telegram


def bot_sending_photo(token, chat_id, path):
    bot = telegram.Bot(token=token)
    with open(path, 'rb') as name_photo:
        bot.send_document(chat_id=chat_id, document=name_photo)


def telegramm_photo_post(bot_token, chat_id, directory, delay):
    files = os.listdir(directory)

    while True:
        for index, photo in enumerate(files):
            bot_sending_photo(bot_token, chat_id, f'{directory}/{files[index]}')
            sleep(delay)
        random.shuffle(files)


def main():
    parser = argparse.ArgumentParser(description='''
        Скрипт выкладывает фото в телеграмм.
        Требует обязательный аргумент, id чата.
        По умолчанию, фото берутся из папки nasa_apod.
        Задержка по умолчанию, 4 часа(3.600 сек).
        Задержка устанавливается в секундах.
    ''')

    parser.add_argument('-chat_id', default='@cosmo_photos')
    parser.add_argument('-d', '--directory', default='nasa_apod')
    parser.add_argument('-t', '--delay', default=3600)
    args = parser.parse_args()

    load_dotenv('TOKENS.env')
    bot_token = os.environ['TELEGRAMM_KEY']

    telegramm_photo_post(bot_token, args.chat_id, args.directory, int(args.delay))


if __name__ == '__main__':
    main()
