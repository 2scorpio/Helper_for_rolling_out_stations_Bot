from aiogram.types import ReplyKeyboardRemove, ContentTypes
import logging
import os


from aiogram import executor, types
from config import dp, bot
from keyboards import in_kb_help, kb_apply_load, in_kb_create_conf


start_massage = 'Привет <b> !Добавить имя! </b>, я могу:\n'\
                "1 - Добавить новый сервер\n" \
                "2 - Добавить камеры на действующий сервер\n"\
                "3 - Изменить значение поля place_name (Только SQL)\n"\
                "4 - Изменить значение поля camera (Только SQL)\n"\
                "5 - Удалить данные в БД (Только SQL)\n"\
                "6 - Обновить поля camera и place_name (С инвентори для перенастройки сервера)\n"\
                "\n"\
                "Для работы со мной нужно загрузить актуальны файл Metro.xlsx, \n"\
                "в противном случае я буду использовать старые данные \n "\
                "после выбора одного из действий вы получите 3 файла конфигурации.\n "\
                "\n "\
                "<b>Итак! Что вы хотите?</b>"



# Configure logging
logging.basicConfig(level=logging.INFO)
file_filler = 'лупа пупа' # Тот, кто последний залил файл
last_date_load = '2023-05-06-20:22'



@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    """ Стартовое приветсвие """
    user = message.from_user # Обращаемся к пользователю
    username = user.username # Берём имя пользователя
    await message.answer(start_massage, reply_markup=in_kb_help)
    await message.delete() # раскомитить после отладки


@dp.callback_query_handler(text="back")
async def go_home_callback(callback: types.CallbackQuery):
    """ Дублирует start_cmd, для кнопки назад """
    await callback.message.answer(start_massage, reply_markup=in_kb_help)
    await bot.answer_callback_query(callback_query_id=callback.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло
    # await callback.message.edit_reply_markup() # Удаляет клаву при нажатии
    await callback.message.delete() # удаляет сообщение


@dp.callback_query_handler(text="PUSH_FILE")
async def reload_file(callback: types.CallbackQuery):
    """ Загрузчик файла """
    await callback.message.answer("Отлично, загрузите файл и нажмите кнопку применить\n"
                                  f'Последний файл был загружен <b>{file_filler}</b> <b>{last_date_load}</b>',
                                  reply_markup=kb_apply_load
                                  )
    await bot.answer_callback_query(callback_query_id=callback.id) # Фиксим часы, отправляем боту ответ, что сообщение дошло
    await callback.message.delete() # удаляет сообщение
    # await callback.message.edit_reply_markup()  # Удаляет клаву при нажатии


@dp.callback_query_handler(text="CREATE_CONF")
async def create_config(callback: types.CallbackQuery):
    """ Создать коонфиги """
    await callback.message.answer("Выберите предложенное дейсвите:",
                                  reply_markup=in_kb_create_conf
                                  )
    await bot.answer_callback_query(callback_query_id=callback.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло
    await callback.message.delete() # удаляет сообщение
    # await callback.message.edit_reply_markup()  # Удаляет клаву при нажатии


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def download_xlsx(file: types.File):
    if file == 'Metro.xlsx':
        destination = r"C:\Metro.xlsx"

        await file.download(destination)














# @dp.message_handler()
# async def echo(message: types.Message):
#     """ Эхо """
#     await message.answer(
#         "Выберите одно из предложенных действий или воспользуйтесь командой /start.",
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await message.delete()
@dp.message_handler()
async def go_home_callback(message: types.Message):
    """ Эхо """
    await message.answer(start_massage, reply_markup=in_kb_help)
    #await bot.answer_callback_query(callback_query_id=callback.id)  # Фиксим часы, отправляем боту ответ, что сообщение дошло
    # await callback.message.edit_reply_markup() # Удаляет клаву при нажатии
    await message.delete() # удаляет сообщение




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
