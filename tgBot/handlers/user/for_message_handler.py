from aiogram import Dispatcher
from aiogram.types import Message
from tgBot.keyboards.inline import inline_kbr_start_menu
from tgBot.misc.text_for_messages import start_massage


# async def first_blood(msg: Message): # её нужно перенести
#     """ Функция для 1‑го запуска """
#     print("Я в first_blood")
#     await msg.delete() # удаляет предыдущее сообщение пользователя


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрация хендлеров """
    #dp.register_message_handler(first_blood, commands=['start'])
