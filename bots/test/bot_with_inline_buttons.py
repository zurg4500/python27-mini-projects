
import telebot
from decouple import config


token = config('TOKEN')
# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBY9kBYcPC2hM5TfqFKibldH4hjjwdQACYQADWbv8JUh0znlMNhLJLgQ'
no_sticker = 'CAACAgIAAxkBAAEIBYtkBYbzTWt3_idkWMpKXLbZuN9sBQACFAADwDZPE61lmeS5MPY-LgQ'

# Миссис клава под сообщением
keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
x1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
x2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(x1, x2)



bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите себе кнопочку сэр\мэм!', reply_markup=keyboard)

# Функция фильтр, в данном случае разершают все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'yes':
        bot.send_sticker(call.from_user.id, no_sticker)


bot.polling() # - команда запуска телеграмм бота
