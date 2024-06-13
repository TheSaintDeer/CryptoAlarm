from celery import shared_task

from .management.commands.bot import bot
from .services import get_price
from .models import *


@shared_task
def send_msg(chat_id, pair, price):
    bot.send_message(chat_id, f'Price of {pair} is {price}!')
    return True


@shared_task
def create_queue_of_msg():
    for pair in Pair.objects.filter(isUsed=True): 
        for alarm in Alarm.objects.filter(pair=pair):
            price = get_price(pair)['result']['list'][0][4]
            chat_id = alarm.user.chat_id
            send_msg.delay(chat_id, pair.name, price)