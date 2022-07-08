import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from telegrambot import bot

if __name__ == "__main__":
    bot.run_bot()