import requests
from bs4 import BeautifulSoup
import lxml
import telebot


token = "1736982389:AAHWkX5UZbcFluMGM8MyGF87SA1fx5fpn4A"

bot = telebot.TeleBot(token)

welcome_text = "Привет! Качество воздуха в Бишкеке сейчас: "

URL = 'https://www.iqair.com/ru/kyrgyzstan/bishkek'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
aqi_descritpive = soup.find('span', class_ = 'aqi-status__text').getText()
aqi_in_numbers = soup.find('p', class_ = 'aqi-value__value').getText()

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text.lower() == 'привет' or "ghbdtn":
        bot.send_message(message.chat.id, welcome_text   +   aqi_in_numbers + " пунктов."
                          " \n Говоря словами, качество воздуха в категории  "
                         + aqi_descritpive)

bot.polling()
