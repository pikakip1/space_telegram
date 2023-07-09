import os
from dotenv import load_dotenv
import telegram
load_dotenv('TELEGRAMM_TOKEN.env')
token = os.environ['TELEGRAMM_KEY']

bot = telegram.Bot(token=token)

bot.send_message(chat_id='@cosmo_photos', text='Первое фото')
bot.send_document(chat_id='@cosmo_photos', document=open('nasa_apod/apod1.gif', 'rb'))
