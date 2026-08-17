import telebot
import requests

# Bu ýere öz bot tokeniňizi goýuň
TOKEN = "8926438266:AAGLXYmEw1OVRMorYb-XwXKEQpQWzkmhICc"
bot = telebot.TeleBot(TOKEN)

# Start komandasy
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "Salam! Kripto we Birža Botuna Hoş Geldiňiz! 🚀\n\n"
        "Aşakdaky komandalary ulanyp bilersiňiz:\n"
        "/crypto - Hakyky wagtaky Kripto (BTC, ETH, USDT) bahalary\n"
        "/about - Bot barada we hyzmatlar"
    )
    bot.reply_to(message, text)

# Kripto bahalaryny alyp berýän bölüm
@bot.message_handler(commands=['crypto'])
def send_crypto_prices(message):
    try:
        # CoinGecko API arkaly anlyk bahalary çekýäris
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd"
        response = requests.get(url).json()
        
        btc = response['bitcoin']['usd']
        eth = response['ethereum']['usd']
        usdt = response['tether']['usd']
        
        msg = (
            "📈 **Hakyky Wagtaky Kripto Kurslary:**\n\n"
            f"🪙 **Bitcoin (BTC):** ${btc:,}\n"
            f"💎 **Ethereum (ETH):** ${eth:,}\n"
            f"💵 **Tether (USDT):** ${usdt}\n\n"
            "💡 *Söwda we maýa goýum üçin hakyky baha.*"
        )
        bot.reply_to(message, msg, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, "Maglumatlary alyp bolmady, bir azdan täzeden synanyşyň.")

# Beýleki ähli tekstler üçin
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Kripto bahalaryny görmek üçin /crypto diýip ýazyň!")

bot.infinity_polling()
