import telebot
from decouple import config


token = config('TOKEN')
# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBY9kBYcPC2hM5TfqFKibldH4hjjwdQACYQADWbv8JUh0znlMNhLJLgQ'
no_sticker = 'CAACAgIAAxkBAAEIBYtkBYbzTWt3_idkWMpKXLbZuN9sBQACFAADwDZPE61lmeS5MPY-LgQ'


bot = telebot.TeleBot(token)

# миссис клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
x1 = telebot.types.KeyboardButton('Да')
x2 = telebot.types.KeyboardButton('Нет')
keyboard.add(x1, x2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите себе кнопочку сэр\мэм!', 
    reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id, 'Сэр\мэм нажмите на кнопку')
    bot.register_next_step_handler(message, reply_to_button)


bot.polling() # - команда запуска телеграмм бота

