from celery import shared_task

from .management.commands.bot import bot
from .services import get_price


@shared_task
def create_queue_of_msg():
    pass


# @shared_task
# def send_price(chat_id, pair):
#     print('start')
#     price = get_price(pair)
#     bot.send_message(chat_id, f'Price of {pair} is {price}!')
#     print(f"Message was sended to {chat_id}")
#     return f"Message was sended to {chat_id}"