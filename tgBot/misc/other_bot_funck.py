import os

from aiogram import types
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound, MessageToDeleteNotFound, \
    MessageNotModified
from config import bot
from tgBot.utility.main import locate


async def delete_inline_and_msg(msg):
    """ Удаление инлай клавиатуры и предыдущего сообщения """
    try:
        await msg.delete()  # удаляет сообщение от пользователя
    except MessageToEditNotFound:
        # print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
        # print("Сообщение для удаления не найдено")
        pass
    except MessageCantBeEdited:
        # print("Сообщение не может быть отредактировано")
        pass
    except MessageNotModified:
        # print("Сообщение для удаления не найдено")
        pass
    chat_id = msg.chat.id
    message_id = msg.message_id - 1 # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    try:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой
    except MessageCantBeEdited:
        # print("Сообщение не может быть отредактировано")
        pass
    except MessageToEditNotFound:
        # print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
        # print("Сообщение для удаления не найдено")
        pass
    except MessageNotModified:
        # print("Сообщение для удаления не найдено")
        pass


async def delete_inline_key_only_last_msg(msg):
    """ Удаление инлай клавиатуры """
    try:
        await msg.message.edit_reply_markup()
    except MessageToEditNotFound:
        # print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
        # print("Сообщение для удаления не найдено")
        pass
    except MessageCantBeEdited:
        # print("Сообщение не может быть отредактировано")
        pass
    except MessageNotModified:
        # print("Сообщение для удаления не найдено")
        pass


async def delete_message_only(msg):
    """ Удаление предыдущего сообщения """
    try:
        await msg.delete()  # удаляет сообщение от пользователя
    except MessageToEditNotFound:
        # print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
         # print("Сообщение для удаления не найдено")
        pass
    except MessageCantBeEdited:
        # print("Сообщение не может быть отредактировано")
        pass
    except MessageNotModified:
        # print("Сообщение для удаления не найдено")
        pass


async def delete_inline_key_only_first_msg(msg):
    """ Удаление инлай клавиатуры """
    chat_id = msg.chat.id
    message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    try:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой
    except MessageCantBeEdited:
        # print("Сообщение не может быть отредактировано")
        pass
    except MessageToEditNotFound:
        # print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
        # print("Сообщение для удаления не найдено")
        pass
    except MessageNotModified:
        # print("Сообщение для удаления не найдено")
        pass


async def delete_file_in_output():
    output = os.path.join(locate, 'data', 'output')
    files = os.listdir(output)
    for file in files:
        os.remove(file)