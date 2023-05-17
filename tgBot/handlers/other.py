from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound

from config import bot
from kbr import inline_kbr_start_menu


async def echo(msg: Message) -> None:
    """ Эхо функция """
    print("Я в echo")

    await msg.delete()  # удаляет сообщение от пользователя

    chat_id = msg.chat.id
    message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    try:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                            reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой
    except MessageCantBeEdited:
        print("Сообщение не может быть отредактировано")
    except MessageToEditNotFound:
        print("Сообщение для редактирования не найдено")

    await msg.answer('Как будет действовать хацкер?\nПоследний файл был загружен КЕМ и КОГДА',
                     reply_markup=inline_kbr_start_menu)


def register_other_handlers(dp: Dispatcher) -> None:
    """ Регистрация хендлеров """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY) # Указываем сразу все типы контента
