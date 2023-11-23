import telebot, os
from neuronet import predict

TOKEN = os.environ.get("telegram_token")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который использует нейронную сеть для создания предсказаний. Отправьте мне текст, и я сокращу его.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        prediction = predict(message.text)
        bot.send_message(message.chat.id, prediction)
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при предсказании. Пожалуйста, попробуйте еще раз.")
        print(e)

bot.polling()