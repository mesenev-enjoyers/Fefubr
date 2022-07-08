import telebot
from django.db.models import Model

from users.models import CustomUser

token = '5248971660:AAFslLdkO2y6LPV6y-KNo4oLhV1h5dyGfX8'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, '''\
    Привет ✌️
Ты зашёл на бота самого лучшего в мире сайта для айтишников ДВФУ - FEFUBR🌊\n
Введи команду /register\t*Твой никнейм на сайте* чтобы получать уведомления о новых постах на которые ты подписан.\n
Надоели уведомления? Тебе поможет команда /delete  введи её  и избавишься от надоедливых уведомлений!
    ''')


@bot.message_handler(commands=['register'])
def register(message):
    try:
        name = message.text.split()[1]
    except Exception as error:
        print(error)
        bot.send_message(message.chat.id, "Неправильный формат имени!")
        return
    try:
        user = CustomUser.objects.get(username=name)
        bot.send_message(message.chat.id, user)
        if user.telegram != '':
            bot.send_message(message.chat.id, "Данный пользователь уже зарегистрирован в боте!")
            return
        user.telegram = message.chat.id
        user.save()
        bot.send_message(message.chat.id, "Успешно!")

    except Exception as error:
        print(error, f'user: {name}')
        bot.send_message(message.chat.id, "Такого пользователя не существует!")


@bot.message_handler(commands=['delete'])
def delete_user(message):
    id = message.chat.id
    try:
        user = CustomUser.objects.get(telegram=id)
    except Exception as error:
        bot.send_message(message.chat.id, "Вы не подписаны на уведомления!")
        return

    user.telegram = ''
    user.save()
    bot.send_message(message.chat.id, "Вы отписались от уведомлений!")


#  Пофиксить ссылку!
def send_article(chat_id, article, username):
    bot.send_message(chat_id, f'Вышла новая статья от пользователя {username} (http://fefubr.tk/?#/post/{article["id"] })')


def run_bot():
    try:
        print("TelegramBot is ready")
        bot.infinity_polling()
    except Exception as error:
        print(error)