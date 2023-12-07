import telebot
from telebot import types
import requests
TOKEN = '6542089143:AAHs1A07twSiAzSr1kSIM7GV1Zk8YH05mS4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Список команд: /dog, /inline")

@bot.message_handler(commands=['dog'])
def send_dog(message):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_data = response.json()
    dog_url = dog_data['message']
    bot.send_photo(message.chat.id, dog_url)
@bot.message_handler(commands=['inline'])
def inline_keyboard(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('github', url='https://github.com/oktapbang-Killy/')
    btn2 = types.InlineKeyboardButton('balance', callback_data='balance')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'balance':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('вывод', callback_data='withdraw')
        btn2 = types.InlineKeyboardButton('пополнить', callback_data='top_up')
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def sub_callback_handler(call):
    if call.data == 'withdraw':
        bot.send_message(call.message.chat.id, "Вы выбрали вывод.")
    elif call.data == 'top_up':
        bot.send_message(call.message.chat.id, "Вы выбрали пополнение.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
