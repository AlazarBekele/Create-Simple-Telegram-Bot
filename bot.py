import os
import telebot

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler (commands=['greet'])
def greet (message):
  bot.reply_to(message, 'hello')

bot.polling() # keep checking for message