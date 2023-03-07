
import telebot
from decouple import config


token = config('TOKEN')
# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBfZkBazAODD9zdhLfMrjxX7xuiQNkAACHQkAAgi3GQLm460yuypr2y4E'
no_sticker = 'CAACAgIAAxkBAAEIBfpkBazeS2qTu93QyOoaIiEKuHM_lgACGwkAAgi3GQIximZhD7nx2y4E'
photo_1 = 'https://api.kinoart.ru/storage/post/1069/regular_detail_picture-8eee4e98206383fb8066843ac5c247a6.jpg'

# Миссис клава под сообщением
keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
x1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
x2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(x1, x2)



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите себе кнопочку сэр\мэм!', reply_markup=keyboard)

# Функция фильтр, в данном случае разрешают все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
        bot.send_photo(call.from_user.id, photo_1)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)


bot.polling() # - команда запуска телеграмм бота
