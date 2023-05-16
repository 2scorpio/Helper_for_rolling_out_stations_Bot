from aiogram import Dispatcher
from aiogram.types import Message


async def echo(msg: Message):
    # todo: remove echo example:3
    await msg.answer(msg.text)


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрация хендлеров """
    # Эхо функция всегда должна быть внизу
    dp.register_message_handler(echo, content_types=['text'])