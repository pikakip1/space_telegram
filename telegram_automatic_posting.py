import os
import random
import argparse
from dotenv import load_dotenv
from time import sleep
from telegramm_bot import telegramm_photo_post


def auto_post(bot_token, directory, delay):
    file = os.listdir(directory)
    file_number = len(file)
    index = 0

    while True:
        if index == file_number:
            random.shuffle(file)
            index = 0
        telegramm_photo_post(bot_token, f'{directory}/{file[index]}')
        index += 1
        sleep(delay)


def main():
    parser = argparse.ArgumentParser(description='''
    Скрипт выкладывает фото в телеграмм.
    По умолчанию, фото берутся из папки nasa_apod.
    Задержка по умолчанию, 4 часа(3.600 сек).
    Задержка устанавливается в секундах.
    ''')
    parser.add_argument('-d', '--directory', default='nasa_apod')
    parser.add_argument('-t', '--delay')
    args = parser.parse_args()

    load_dotenv('TELEGRAMM_TOKEN.env')
    bot_token = os.environ['TELEGRAMM_KEY']

    load_dotenv('POST_DELAY.env')
    post_delay = os.environ['post_delay']
    delay = args.delay

    if not args.delay:
        delay = int(post_delay)

    auto_post(bot_token, args.directory, int(delay))


if __name__ == '__main__':
    main()
