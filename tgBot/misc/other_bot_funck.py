import os

from aiogram import types
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound, MessageToDeleteNotFound, \
    MessageNotModified
from config import bot
from tgBot.utility.main import locate_tgbot_utility, locate_tgbot_utility_data_output
from tgBot.utility.stationAll_V6 import main_station


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
    message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    try:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                            reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой
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
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                            reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой
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


async def create_send_del_file(callback_query):
    """ Функция запускает скрипт, отправляет доки и удаляет их """
    call = callback_query.data
    await main_station(int(call[-1]))
    files = os.listdir(locate_tgbot_utility_data_output)
    for file in files:
        file_locate = os.path.join(locate_tgbot_utility_data_output, file)  # Локация файла
        with open(file_locate, 'rb') as foo:
            await bot.send_document(callback_query.from_user.id, document=foo)
        os.remove(file_locate)
        #os.remove(file)
