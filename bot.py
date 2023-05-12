from aiogram.types import ReplyKeyboardRemove, ContentTypes
import logging
import os
import shutil



from aiogram import executor, types
from aiogram.utils.exceptions import MessageNotModified, MessageToDeleteNotFound

import bot_func
from bot_func import upload_flag_off, delete_inline_button_in_message_handler, upload_flag_on, go_home_start_menu, \
    start_massage, button_upload_file, locate, upload_flag
from config import dp, bot
from kbr import inline_kbr_start_menu, inline_kbr_upload_new_file, inline_kbr_new_file_apply
from keyboards import in_kb_help, kb_apply_load1, in_kb_create_conf, kb_apply_load2

logging.basicConfig(level=logging.INFO)
# Face_Halper_Bot



@dp.message_handler(commands=['start'])
async def first_blood(msg: types.Message):
    """ Функция для 1‑го запуска """
    await upload_flag_off()
    await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)
    await msg.delete() # удаляет предыдущее сообщение пользователя

####################### Меню #######################
@dp.callback_query_handler(lambda query: query.data.startswith('start_'))
async def start_menu(callback_query: types.CallbackQuery):
    """ Меню старт """
    call = callback_query.data
    if call == 'start_1':
        """ 1. - Добавить новый сервер """
        await call.answer('Вы выбрали Callback 1')
    elif call == 'start_2':
        """ 2. - Добавить новый сервер """
        await call.answer('Вы выбрали Callback 1')
        ######################################
        ######################################
    elif call.startswith('start_Upload'):
        """ Меню обновления файла, вызывается с кнопки "Обновить файл" """
        await button_upload_file(callback_query)
        ######################################
    else:
        """ Заглушка """
        await callback_query.answer('Сорри, разработчика, скорее всего, заставляют работать другую бесполезную работу, выберите пока что ни будь другое. Спасибо за понимание.', show_alert=True)


@dp.callback_query_handler(lambda query: query.data.startswith('upload_'))
async def start_menu(callback_query: types.CallbackQuery):
    """ Меню загрузки | В этом меню документ слушает файл"""
    call = callback_query.data
    if call == 'upload_Download_reference_file':
        """ Кнопка "Скачать образец" """





        await callback_query.message.delete()  # Удаляет сообщение полностью
        # Придумать рекурсию !!!!!!!!!!!!!!!! Дублирует reload_reference_file_1
        await start_menu(callback_query)


        file_ref_locate = os.path.join(locate, 'reference_files', 'Metro.xlsx')
        with open(file_ref_locate, 'rb') as file:
            await bot.send_document(callback_query.from_user.id, file)
        await start_menu(callback_query)



    elif call == 'upload_Back':
        """ Кнопка назад """
        await go_home_start_menu(callback_query)



@dp.callback_query_handler(lambda query: query.data.startswith('apply_'))
async def moving_file(callback_query: types.CallbackQuery):
    """ Меню приминения нового файла """
    call = callback_query.data
    if call == 'apply_Moving_file':
        file = os.path.join(locate, 'temp', 'Metro.xlsx')
        destination_folder = os.path.join(locate, 'data', 'Metro.xlsx')
        await callback_query.answer('Готово!')
        try:
            shutil.move(file, destination_folder)
        except FileNotFoundError:
            await call.answer('Упс, сообщите разработчику, что временный файл протерялся и его обновить не удалось.', show_alert=True)
        await go_home_start_menu(callback_query)
    elif call == 'apply_Back':
        await go_home_start_menu(callback_query)






####################### Служебные #######################
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def listen_file_downloads(msg: types.Message):
    await delete_inline_button_in_message_handler(msg)
    """ Функция слушает документ и загружает его"""
    if bot_func.upload_flag:
        if msg.document.mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':  # and message.document.file_name == 'Metro.xlsx': - Проверка по имени
            file_id = msg.document.file_id
            file_name = 'Metro.xlsx'  # Переопределяем имя
            file_path = await bot.get_file(file_id)  # Скачиваем файл
            downloaded_file = await bot.download_file(file_path.file_path)
            file = os.path.join(locate, 'temp', file_name)
            # Сохраняем файл на сервере
            with open(file, 'wb') as f:
                f.write(downloaded_file.read())
            await msg.answer('Файл успешно загружен, выберите действие.', reply_markup=inline_kbr_new_file_apply)
            await msg.delete()  # удаляет сообщение от пользователя
        else:
            await msg.delete()  # удаляет сообщение от пользователя
            await msg.answer('Не верный формат, загрузите файл в формате XLSX.', reply_markup=inline_kbr_upload_new_file)


@dp.message_handler()
async def go_home_message(msg: types.Message):
    """ Эхо функция """
    await upload_flag_off()
    await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)
    await delete_inline_button_in_message_handler(msg)
    await msg.delete()  # удаляет сообщение от пользователя

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)