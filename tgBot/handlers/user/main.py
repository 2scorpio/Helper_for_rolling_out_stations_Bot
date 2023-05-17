from aiogram import Dispatcher


from aiogram.types import Message
from tgBot.keyboards.inline import inline_kbr_start_menu
from tgBot.misc.text_for_messages import start_massage


async def first_blood(msg: Message) -> None:
    """ Функция для 1‑го запуска """
    print("Я в first_blood")
    await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)


def register_user_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(first_blood, commands=['start'])

