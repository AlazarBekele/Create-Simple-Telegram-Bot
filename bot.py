import os

import telebot

BOT_TOKEN = os.environ.get ('7522950368:AAFhmUZAhZ9XCK_fJ_0leLSlee1IHqoi5TE')

bot = telebot.TeleBot (BOT_TOKEN)


@bot.message_handler(commands=['Start' ,'Hello User'])
def Send_Welcome_message (message):
  bot.reply_to (message, 'Ho! Hello, How are you?')