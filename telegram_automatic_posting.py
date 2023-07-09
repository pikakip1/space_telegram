import os
import random
import argparse
from dotenv import load_dotenv
from time import sleep
import telegram


def telegramm_photo_post(token, chat_id, path):
    bot = telegram.Bot(token=token)

    bot.send_document(chat_id=chat_id, document=open(path, 'rb'))


def get_photo_path(bot_token,chat_id, directory, delay):
    file = os.listdir(directory)
    file_number = len(file)
    index = 0

    while True:
        if index == file_number:
            random.shuffle(file)
            index = 0
        telegramm_photo_post(bot_token, chat_id, f'{directory}/{file[index]}')
        index += 1
        sleep(delay)


def main():
    parser = argparse.ArgumentParser(description='''
    Скрипт выкладывает фото в телеграмм.
    Требует обязательный аргумент, id чата.
    По умолчанию, фото берутся из папки nasa_apod.
    Задержка по умолчанию, 4 часа(3.600 сек).
    Задержка устанавливается в секундах.
    ''')

    parser.add_argument('chat_id')
    parser.add_argument('-d', '--directory', default='nasa_apod')
    parser.add_argument('-t', '--delay')
    args = parser.parse_args()

    load_dotenv('TELEGRAMM_TOKEN.env')
    bot_token = os.environ['TELEGRAMM_KEY']
    delay = args.delay

    if not args.delay:
        file_delay = open('POST_DELAY.txt')
        delay = file_delay.read()
        file_delay.close()

    get_photo_path(bot_token,args.chat_id, args.directory, int(delay))


if __name__ == '__main__':
    main()
