import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello Анимэшник!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBUxkBXahy-p6JoXXlI15RnbNTfuFlAACMQADO2AkFAuPDYcNLFRQLgQ')
    bot.send_photo(message.chat.id, 'https://ru.dreamstime.com/%D1%84%D1%83%D1%82%D1%83%D1%80%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%84%D0%BE%D0%BD-%D1%81%D0%B8%D0%BD%D0%B5%D0%B9-%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8-sci-fi-%D0%BA%D0%B0%D0%B4%D1%80-hud-ui-%D1%82%D0%B5%D0%BC%D0%B0-%D0%BD%D0%B8%D0%B6%D0%BD%D1%8F%D1%8F-%D1%82%D1%80%D0%B5%D1%82%D1%8C%D1%8F-image225367935')

@bot.message_handler(content_types=['text'])
def xxx(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет Анимэшник')
    else:
        bot.send_message(message.chat.id, 'Анимэшник твое сообщение не распознанно')

def yyy(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)

bot.polling()

