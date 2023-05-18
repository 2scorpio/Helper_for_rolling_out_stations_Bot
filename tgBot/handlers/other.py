from aiogram import Dispatcher, types
from aiogram.types import Message
from kbr import inline_kbr_start_menu
from tgBot.misc.other_bot_funck import delete_inline_button_in_message_handler


async def echo(msg: Message) -> None:
    """ Эхо функция """
    print("Я в echo")
    await msg.delete()  # удаляет сообщение от пользователя
    await delete_inline_button_in_message_handler(msg)  # Удаление инлай клавиатуры с предыдущего сообщения для message_handler
    await msg.answer('Как будет действовать хацкер?\nПоследний файл был загружен КЕМ и КОГДА',
                     reply_markup=inline_kbr_start_menu)


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY) # Указываем сразу все типы контента
