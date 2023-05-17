from aiogram import Dispatcher, types

from aiogram.types import Message
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound

from config import bot
from tgBot.keyboards.inline import inline_kbr_start_menu


async def first_blood(msg: Message) -> None:
    """ Функция для 1‑го запуска """
    print("Я в first_blood")
    await msg.delete()  # удаляет предыдущее сообщение пользователя

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



def register_user_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(first_blood, commands=['8'])
    dp.register_message_handler(first_blood, content_types=['text'], text="8")
