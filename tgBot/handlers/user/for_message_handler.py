from aiogram import Dispatcher
from aiogram.types import Message
from ...keyboards.inline import inline_kbr_start_menu
from ...misc.messages import start_massage


async def first_blood(msg: Message): # её нужно перенести
    """ Функция для 1‑го запуска """
    await msg.delete() # удаляет предыдущее сообщение пользователя
    # await delete_inline_button_in_message_handler(msg) # Добавить позже
    # await upload_flag_off() # Добавить позже
    await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)


def register_message_handlers(dp: Dispatcher) -> None:
    """ Регистрация хендлеров """
    dp.register_message_handler(first_blood, commands=['start'])
