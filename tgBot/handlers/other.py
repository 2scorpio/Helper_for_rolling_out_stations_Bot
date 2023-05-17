from aiogram import Dispatcher, types
from aiogram.types import Message

from tgBot.handlers.user.main import first_blood
#from tgBot.misc.states import flag_Main_menu

flag_Main_menu = True

async def echo(msg: Message) -> None:
    """ Эхо функция """
    if flag_Main_menu:
        await msg.delete()  # удаляет сообщение от пользователя
    else:
    # await upload_flag_off()
    # await delete_inline_button_in_message_handler(msg)
        await first_blood(msg)  # Вызов стартового меню


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрация хендлеров """

    # Эхо функция всегда должна быть внизу
    dp.register_message_handler(echo, content_types=types.ContentType.ANY) # Указываем сразу все типы контента
