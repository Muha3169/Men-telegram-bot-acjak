import telebot

# BotFather-den alan tokeniňizi şu ýere ýazyň
bot = telebot.TeleBot("8926438266:AAGLXYmEw10VRMorYb-XwXKEQpQWzkmhICc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Men işleýärin! Bu meniň ilkinji botum.")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Siz şuny ýazdyňyz: " + message.text)

bot.polling()
