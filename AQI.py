import requests
from bs4 import BeautifulSoup
import telebot


token = "1736982389:AAFWK5rYZqHVeEMzDZ94Aw3VJSBX9q2WFLo"
bot = telebot.TeleBot(token)

URL = 'https://aqicn.org/city/kyrgyzstan/bishkek/us-embassy/'

response = requests.get(URL, 'lxml')
soup = BeautifulSoup(response.content, 'lxml')
items = soup.find('div', {'id': "aqiwgtvalue"})
text_1 = items.text
print(text_1)

welcome_text = "Привет! Качество воздуха в Бишкеке сейчас: "

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, welcome_text   +   text_1 + " пунктов." + " Чтобы узнать больше, посети сайт https://aqicn.org/map/bishkek/ru/")

bot.polling()
