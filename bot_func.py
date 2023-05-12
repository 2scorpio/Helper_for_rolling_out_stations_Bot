""" Общие функции и глобальные переменные """
from aiogram.types import ReplyKeyboardRemove, ContentTypes
import logging
import os
import shutil

from aiogram import executor, types
from config import dp, bot
from kbr import inline_kbr_upload_new_file, inline_kbr_start_menu, inline_kbr_new_file_apply
from keyboards import in_kb_help, kb_apply_load1, in_kb_create_conf, kb_apply_load2

locate = os.path.dirname(__file__)
start_massage = 'Как будет действовать хацкер?\nПоследний файл был загружен КЕМ и КОГДА'
upload_flag = False  # Флаг загрузки


async def delete_inline_button_in_message_handler(msg):
    await msg.delete()  # удаляет сообщение
    """ Удаление инлай клавиатуры с предыдущего сообщения для message_handler """
    chat_id = msg.chat.id
    message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                        reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой


async def upload_flag_off():
    """ Выключает флаг загрузки, должна быть установлена каждую функцию, кроме меню загрузки файла """
    global upload_flag
    upload_flag = False


async def upload_flag_on():
    """ Включает флаг загрузки """
    global upload_flag
    upload_flag = True


async def go_home_start_menu(callback: types.CallbackQuery):
    """ Кнопка назад стартового меню """
    await upload_flag_off()
    await callback.message.edit_reply_markup()  # Удаляет клавиатуру при нажатии
    await callback.message.answer(start_massage, reply_markup=inline_kbr_start_menu)



async def reload_reference_file(callback: types.CallbackQuery):
    """ Скачивание файла референса"""
    file_ref_locate = os.path.join(locate, 'reference_files', 'Metro.xlsx')
    with open(file_ref_locate, 'rb') as file:
        await bot.send_document(callback.from_user.id, file)
    await bot.answer_callback_query(
        callback_query_id=callback.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло


async def button_upload_file(callback_query):
    await upload_flag_on()
    await callback_query.message.answer('Бот ожидает загрузи файла', reply_markup=inline_kbr_upload_new_file)
    await callback_query.message.edit_reply_markup()  # Удаляет клавиатуру при нажатии


async def replace_file(call: types.CallbackQuery):
    """ Заменят старый файл на новый """
    file = os.path.join(locate, 'temp', 'Metro.xlsx')
    destination_folder = os.path.join(locate, 'data', 'Metro.xlsx')
    try:
        shutil.move(file, destination_folder)
    except FileNotFoundError:
        await call.answer('Упс, сообщите разработчику, что временный файл протерялся и его обновить не удалось.',
                              show_alert=True)
    await go_home_start_menu(call)
