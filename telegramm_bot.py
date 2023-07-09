import telegram


def telegramm_photo_post(token, path):
    bot = telegram.Bot(token=token)

    bot.send_document(chat_id='@cosmo_photos', document=open(path, 'rb'))

