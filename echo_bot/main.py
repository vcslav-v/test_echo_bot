import telebot

bot = telebot.TeleBot('')


@bot.message_handler(content_types=['text', 'photo', 'document'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message)


if __name__ == '__main__':
     bot.infinity_polling()
