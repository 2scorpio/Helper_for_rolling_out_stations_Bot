from aiogram import types
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound, MessageToDeleteNotFound, \
    MessageNotModified
from config import bot


async def delete_inline_and_msg(msg): # Удаляет только из под message_handler
    """ Удаление инлай клавиатуры с предыдущего сообщения для message_handler """
    await msg.delete()  # удаляет сообщение от пользователя
    chat_id = msg.chat.id
    message_id = msg.message_id - 1 # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    try:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой
    except MessageCantBeEdited:
        print("Сообщение не может быть отредактировано")
        pass
    except MessageToEditNotFound:
        print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
        print("Сообщение для удаления не найдено")
        pass
    except MessageNotModified:
        print("Сообщение для удаления не найдено")
        pass


async def delete_inline_key_only(callback_query): # Удаляет только из под message_handler
    try:
        await callback_query.message.edit_reply_markup()
    except MessageToEditNotFound:
        print("Сообщение для редактирования не найдено")
    except MessageToDeleteNotFound:
        print("Сообщение для удаления не найдено")
        pass
    except MessageCantBeEdited:
        print("Сообщение не может быть отредактировано")
        pass
    except MessageNotModified:
        print("Сообщение для удаления не найдено")
        pass

