import os
import telebot

# Bot tokenini alýarys
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# /start komandasy üçin
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Men täzelenen akylly bot. Size näme kömek edip bilerin?")

# Ulanyjynyň ýazan habarlaryna jogap bermek
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    
    if "salam" in text:
        bot.reply_to(message, "Salam! Ýagdaýlaryňyz gowymy?")
    elif "dollar" in text or "manat" in text:
        bot.reply_to(message, "Maliýe we kurslar barada maglumatlar basym goşular!")
    elif "kripto" in text or "binance" in text:
        bot.reply_to(message, "Kripto bazary baradaky täzelikler taýýarlanylýar.")
    else:
        bot.reply_to(message, f"Düşündim! '{message.text}' diýip ýazdyňyz. Tiz arada bu tema boýunça giňişleýin jogaplar goşular.")

# Boty işletmek
if __name__ == "__main__":
    bot.infinity_polling()
