from aiogram import Dispatcher, types
from aiogram.types import Message


async def echo(msg: Message) -> None:
    """ Эхо функция """
    print("Я в echo")
    await msg.delete()  # удаляет сообщение от пользователя


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрация хендлеров """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY) # Указываем сразу все типы контента
