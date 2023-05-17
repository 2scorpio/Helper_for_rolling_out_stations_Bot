from aiogram import Dispatcher, types
from aiogram.types import Message


async def echo(msg: Message):
    """ Эхо функция """
    # await upload_flag_off()
    # await delete_inline_button_in_message_handler(msg)
    # await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)  # Вызов стартового меню
    await msg.delete()  # удаляет сообщение от пользователя


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрация хендлеров """

    # Эхо функция всегда должна быть внизу
    dp.register_message_handler(echo, content_types=types.ContentType.ANY) # Указываем сразу все типы контента
