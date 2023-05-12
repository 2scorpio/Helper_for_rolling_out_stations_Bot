from aiogram.types import ReplyKeyboardRemove, ContentTypes
import logging
import os
import shutil



from aiogram import executor, types
from aiogram.utils.exceptions import MessageNotModified, MessageToDeleteNotFound

from bot_func import upload_flag_off, delete_inline_button_in_message_handler, upload_flag_on, go_home_start_menu, \
    start_massage, reload_reference_file, button_upload_file, upload_flag, locate, load_file, moving_file
from config import dp, bot
from kbr import inline_kbr_start_menu, inline_kbr_upload_new_file, inline_kbr_new_file_apply
from keyboards import in_kb_help, kb_apply_load1, in_kb_create_conf, kb_apply_load2

logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['start'])
async def first_blood(msg: types.Message):
    """ Функция для 1‑го запуска """
    await upload_flag_off()
    await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)
    await msg.delete() # удаляет предыдущее сообщение пользователя


@dp.callback_query_handler(lambda query: query.data.startswith('call_'))
async def start_menu(callback_query: types.CallbackQuery):
    """ callback_query_handler Для меню стартового меню """
    call = callback_query.data
    if call == 'call_1':
        """ 1. - Добавить новый сервер """
        await call.answer('Вы выбрали Callback 1')
    elif call == 'call_2':
        """ 2. - Добавить новый сервер """
        await call.answer('Вы выбрали Callback 1')
    elif call.startswith('call_upload'):
        """ Меню обновления файла, вызывается с кнопки "Обновить файл", сама кнопка в блоке Else """
        if call.startswith('call_upload_'):
            if call == 'call_upload_Back':
                """ Кнопка назад """
                await go_home_start_menu(callback_query)
            elif call == 'call_upload_Download_reference_file':
                """ Кнопка "Скачать образец" """
                await reload_reference_file(callback_query)
            elif call.startswith('call_upload_moving_'):
                if call == 'call_upload_moving_file':
                    """ Кпопка "Применить файл """
                    await moving_file(callback_query)

        else:
            """ Кнопка "Обновить файл" """
            await button_upload_file(callback_query)
    else:
        """ Заглушка """
        await callback_query.answer('Сорри, разработчика, скорее всего, заставляют работать другую бесполезную работу, выберите пока что ни будь другое. Спасибо за понимание.', show_alert=True)












@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def listen_file_downloads(msg: types.Message):
    """ Функция слушает документы """
    await load_file(msg)


@dp.message_handler()
async def go_home_message(msg: types.Message):
    """ Эхо функция """
    await upload_flag_off()
    await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)
    await msg.delete()  # удаляет предыдущее сообщение пользователя
    chat_id = msg.chat.id
    message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                        reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)