""" Общие функции и глобальные переменные """
from aiogram.types import ReplyKeyboardRemove, ContentTypes
import logging
import os
import shutil

from aiogram import executor, types
from config import dp, bot
from kbr import inline_kbr_upload_new_file, inline_kbr_start_menu, inline_kbr_new_file_apply


locate = os.path.dirname(__file__)
start_massage = 'Как будет действовать хацкер?\nПоследний файл был загружен КЕМ и КОГДА'
upload_flag = False  # Флаг загрузки
last_massage_with_inline_kbrd = 0
chat_id = 0
message_id = 0


# async def delete_inline_button_in_message_handler(msg): # Удаляет только из под message_handler
#     """ Удаление инлай клавиатуры с предыдущего сообщения для message_handler """
#     chat_id = msg.chat.id
#     message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
#     reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
#     await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
#                                         reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой


async def upload_flag_off():
    """ Выключает флаг загрузки, должна быть установлена каждую функцию, кроме меню загрузки файла """
    global upload_flag
    upload_flag = False


async def upload_flag_on():
    """ Включает флаг загрузки """
    global upload_flag
    upload_flag = True


async def go_home_start_menu(call: types.CallbackQuery):
    """ Кнопка назад стартового меню """
    await upload_flag_off()
    await call.message.edit_reply_markup()  # Удаляет клавиатуру при нажатии
    await call.message.answer(start_massage, reply_markup=inline_kbr_start_menu)



async def reload_reference_file_1(call: types.CallbackQuery):
    """ Скачивание файла референса"""
    #await call.message.edit_reply_markup()  # Удаляет клавиатуру при нажатии
    await call.message.delete()  # Удаляет сообщение полностью
    file_ref_locate = os.path.join(locate, 'reference_files', 'Metro.xlsx')
    with open(file_ref_locate, 'rb') as file:
        await bot.send_document(call.from_user.id, file)
    await bot.answer_callback_query(callback_query_id=call.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло


async def button_upload_file(callback_query):
    await upload_flag_on()
    await callback_query.message.answer('Бот ожидает загрузки файла', reply_markup=inline_kbr_upload_new_file)
    await callback_query.message.edit_reply_markup()  # Удаляет клавиатуру при нажатии


def get_id_last_massage_with_inline_kbrd(msg):
    """ Функция получает id предыдущего сообщения с инлайн кнопкой и записывает текущее сообщение """
    """ Функцию нужно вставлять перед сообщением бота """
    with open('HDD', 'r', encoding='UTF-8') as file: # Получаем id предыдущего сообщения
        last_massage_with_inline_kbrd = file.read().split(' ')
    with open('HDD', 'w', encoding='UTF-8') as file: # Получаем id сообщения и записываем его
        file.write(f'{msg.chat.id} {msg.message_id + 1}')
    return last_massage_with_inline_kbrd
