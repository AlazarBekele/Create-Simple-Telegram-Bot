import os
import telebot


BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler (commands=['greet'])
def greet (message):
  bot.reply_to(message, 'Hey! hello how are you?')


@bot.message_handler (commands=['hello'])
def hello (message):
  bot.send_message (message.chat.id, 'Hello!')

bot.polling() # keep checking for message