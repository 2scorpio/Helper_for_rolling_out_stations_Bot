from aiogram import Dispatcher, types
from aiogram.types import Message

from tgBot.handlers.user.main import first_blood
from tgBot.keyboards.inline import inline_kbr_start_menu
from tgBot.misc.other_bot_funck import delete_inline_button_in_message_handler
from tgBot.misc.text_messages import start_menu_massage


async def echo(msg: Message) -> None:
    """ Эхо функция """
    print("Я в echo")
    await delete_inline_button_in_message_handler(msg)  # Удаление инлай клавиатуры с предыдущего сообщения для message_handler
    await msg.delete()  # удаляет сообщение от пользователя
    await first_blood(msg)


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY)  # Указываем сразу все типы контента
