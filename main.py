from aiogram.types import ReplyKeyboardRemove, ContentTypes
import logging
import os


from aiogram import executor, types
from config import dp, bot
from keyboards import in_kb_help, kb_apply_load1, in_kb_create_conf, kb_apply_load2

start_massage = 'Привет <b> !Добавить имя! </b>, я могу:\n'\
                "1 - Добавить новый сервер\n" \
                "2 - Добавить камеры на действующий сервер\n"\
                "3 - Изменить значение поля place_name (Только SQL)\n"\
                "4 - Изменить значение поля camera (Только SQL)\n"\
                "5 - Удалить данные в БД (Только SQL)\n"\
                "6 - Обновить поля camera и place_name (С инвентори для перенастройки сервера)\n"\
                "\n"\
                "Для работы со мной нужно загрузить актуальный файл Metro.xlsx, \n"\
                "в противном случае я буду использовать старые данные \n "\
                "после выбора одного из действий вы получите 3 файла конфигурации.\n "\
                "\n "\
                "<b>Итак! Что вы хотите?</b>"




# Configure logging
logging.basicConfig(level=logging.INFO)
file_filler = 'лупа пупа' # Тот, кто последний залил файл
last_date_load = '2023-05-06-20:22'
upload_flag = False # Флаг загрузки

""" Удаление инлай клавиатуры с предыдущего сообщения для message_handler """
async def delete_in_keyboard(msg):
    await msg.delete()  # удаляет сообщение
    """ Удаление инлай клавиатуры с предыдущего сообщения для message_handler """
    chat_id = msg.chat.id
    message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                        reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой


async def upload_flag_off():
    """ Выключает флаг загрузки, должа быть установлена каждую функцию, кроме меню загрузки файла """
    global upload_flag
    upload_flag = False

async def upload_flag_on():
    """ Включает флаг загрузки """
    global upload_flag
    upload_flag = True


""" Функции кторые потом перенсти """





@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    """ Стартовое приветсвие """
    await upload_flag_off()
    # user = message.from_user # Обращаемся к пользователю
    # username = user.username # Берём имя пользователя
    await message.answer(start_massage, reply_markup=in_kb_help)
    await message.delete() # раскомитить после отладки



@dp.callback_query_handler(text="back")
async def go_home_callback(callback: types.CallbackQuery):
    """ Дублирует start_cmd, для кнопки назад """
    await upload_flag_off()
    await callback.message.answer(start_massage, reply_markup=in_kb_help)
    await bot.answer_callback_query(callback_query_id=callback.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло
    await callback.message.edit_reply_markup() # Удаляет клаву при нажатии
    # await callback.message.delete() # удаляет сообщение


@dp.callback_query_handler(text="PUSH_FILE")
async def reload_file(callback: types.CallbackQuery):
    """ Загрузчик файла, меню 1"""
    await upload_flag_on()
    await callback.message.answer("Отлично, бот ожидает загрузи, загрузите файл\n"
                                  f'Последний файл был загружен <b>{file_filler}</b> <b>{last_date_load}</b>',
                                  reply_markup=kb_apply_load1
                                  )
    await bot.answer_callback_query(callback_query_id=callback.id) # Фиксим часы, отправляем боту ответ, что сообщение дошло
    # await callback.message.delete() # удаляет сообщение
    await callback.message.edit_reply_markup()  # Удаляет клаву при нажатии



@dp.callback_query_handler(text="CREATE_CONF")
async def create_config(callback: types.CallbackQuery):
    """ Создать коонфиги """
    await upload_flag_off()
    await callback.message.answer("Выберите предложенное дейсвите:",
                                  reply_markup=in_kb_create_conf
                                  )
    await bot.answer_callback_query(callback_query_id=callback.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло
    # await callback.message.delete() # удаляет сообщение
    await callback.message.edit_reply_markup()  # Удаляет клаву при нажатии


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def process_xlsx(message: types.Message):
    """ Загрузка файла, меню 2 """
    if upload_flag:
        if message.document.mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': #and message.document.file_name == 'Metro.xlsx': - Проверка по имени
            file_id = message.document.file_id
            file_name = message.document.file_name
            # Скачиваем файл
            file_path = await bot.get_file(file_id)
            downloaded_file = await bot.download_file(file_path.file_path)
            # Сохраняем файл на сервере
            with open(file_name, 'wb') as f:
                f.write(downloaded_file.read())
            await message.answer('Файл успешно загружен, выберите действие.', reply_markup=kb_apply_load2)
            await delete_in_keyboard(message)
        else:
            await message.answer('Пожалуйста, загрузите файл в формате XLSX.')
            await delete_in_keyboard(message)
















# @dp.message_handler()
# async def echo(message: types.Message):
#     """ Эхо """
#     await message.answer(
#         "Выберите одно из предложенных действий или воспользуйтесь командой /start.",
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await message.delete()
@dp.message_handler()
async def go_home_callback(msg: types.Message):
    """ Эхо """
    await upload_flag_off()
    await msg.answer(start_massage, reply_markup=in_kb_help)
    #await bot.answer_callback_query(callback_query_id=callback.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло
    await delete_in_keyboard(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
