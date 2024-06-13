import re

from typing import Dict
import telebot
from telebot.types import Message
from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import TelegramChat, Pair, Alarm
from core.services import get_price

import core.management.commands.messages as m
from core.management.commands.messages import list_alarms


bot = telebot.TeleBot(settings.API_KEY)
context: Dict[int, Dict[str, str]] = dict()

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    TelegramChat.objects.get_or_create(chat_id=message.chat.id)
    bot.send_message(message.chat.id, m.user_start_answer)

@bot.message_handler(commands=['help'])
def send_welcome(message: Message):
    bot.send_message(message.chat.id, m.help_answer)

def create_alarm(message: Message):
    global context
    if message.chat.id not in context:
        context[message.chat.id] = dict()

    if 'requested' in context[message.chat.id]:
        try:
            if get_price(message.text):
                chat = TelegramChat.objects.get(
                    chat_id=message.chat.id
                )
                pair, _ = Pair.objects.get_or_create(
                    name=message.text
                )
                Alarm.objects.create(
                    user=chat,
                    pair=pair,
                )
                bot.send_message(message.chat.id, 'The alarm has been set successfully.')
                context[message.chat.id] = dict()
                return
                
        except:
            bot.send_message(message.chat.id, f'I couldn\'t find \'{message.text}\' =(.')
            return

    else:
        context[message.chat.id] = {"requested": "1"}
        bot.send_message(message.chat.id, "Enter the pair of coins you are interested in:")
        bot.register_next_step_handler(message, create_alarm)

@bot.message_handler(commands=['new_alarm'])
def new_alarm(message: Message):
    create_alarm(message)

@bot.message_handler(commands=['my_alarms'])
def my_alarms(message: Message):
    user = TelegramChat.objects.get(chat_id=message.chat.id)
    alarms = Alarm.objects.filter(user=user)
    if alarms:
        bot.send_message(message.chat.id, 'Your alarms:\n\n'+list_alarms(alarms))
    else:
        bot.send_message(message.chat.id, 'You have any alarm.')

def delete_alarm_by_id(message: Message, alarms: list):
    if re.search('^\d*$', message.text):
        try:
            alarm_id = int(message.text)-1
            alarms[alarm_id].delete()
            bot.send_message(message.chat.id, 'Alarm was deleted.')
            return
        except:
            bot.send_message(message.chat.id, 'There is no such alarm number.')
            return
    else:
        bot.send_message(message.chat.id, 'Incorrect alarm number.')
        return

@bot.message_handler(commands=['delete_alarm'])
def delete_alarm(message: Message):
    user = TelegramChat.objects.get(chat_id=message.chat.id)
    alarms = Alarm.objects.filter(user=user)
    if alarms:
        bot.send_message(message.chat.id, 'Select the alarm clock you want to delete:\n\n'+list_alarms(alarms))
        bot.register_next_step_handler(message, delete_alarm_by_id, alarms)
    else: 
        bot.send_message(message.chat.id, 'You have any alarm.')

def delete_all(alarms: list):
    for alarm in alarms:
        alarm.delete()

@bot.message_handler(commands=['delete_all_alarms'])
def delete_all_alarms(message: Message):
    user = TelegramChat.objects.get(chat_id=message.chat.id)
    alarms = Alarm.objects.filter(user=user)
    delete_all(alarms)
    bot.send_message(message.chat.id, 'All alarms have been deleted successfully.')

@bot.message_handler(commands=['my_id'])
def print_id(message: Message):
    bot.send_message(message.chat.id, f'Your chat id is {message.chat.id}')

class Command(BaseCommand):
    help = "Run the bot"
    
    def handle(self, *args, **options):
        bot.polling()