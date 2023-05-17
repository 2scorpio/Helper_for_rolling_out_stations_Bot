from aiogram import Dispatcher, types

from aiogram.types import Message
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound

from config import bot
from tgBot.keyboards.inline import inline_kbr_start_menu
from tgBot.misc.other_funck import delete_inline_button_in_message_handler
from tgBot.misc.text_for_messages import start_massage
from tgBot.misc.states import flag_Main_menu


async def first_blood(msg: Message, state: flag_Main_menu) -> None:
    """ Функция для 1‑го запуска """
    if state:
        await msg.delete()  # удаляет предыдущее сообщение пользователя
    else:

        await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)
        await msg.delete()  # удаляет предыдущее сообщение пользователя
        await delete_inline_button_in_message_handler(msg)
        state = True


    # await delete_inline_button_in_message_handler(msg) # Добавить позже
    # await upload_flag_off() # Добавить позже
    # await msg.delete()  # удаляет предыдущее сообщение пользователя



def register_user_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(first_blood, commands=['start'], state=flag_Main_menu)
    dp.register_message_handler(first_blood, content_types=["text"], text="start", state=flag_Main_menu)


    """ Пример """
    # dp.register_message_handler(__start, commands=["start"])
    # dp.register_message_handler(__teh_support, content_types=["text"], text="Тех-поддержка ⚙")
    # dp.register_message_handler(__help, content_types=['text'], text="Узнать команды 📌")
    # _register_vip_handlers(dp)
    # _register_user_bot_handlers(dp)