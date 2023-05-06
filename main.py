import logging
import os

from aiogram import executor, types
from config import dp, bot
from keyboards import kb_help, kb_apply_load


# Configure logging
logging.basicConfig(level=logging.INFO)
file_filler = 'лупа пупа' # Тот, кто последний залил файл
last_date_load = '2023-05-06-20:22'

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    user = message.from_user # Обращаемся к пользователю
    username = user.username # Берём имя пользователя
    await message.answer(
                        f"Привет <b>{username}</b>, я могу:\n"
                        '1 - Добавить новый сервер\n'
                        '2 - Добавить камеры на действующий сервер\n'
                        '3 - Изменить значение поля place_name (Только SQL)\n'
                        '4 - Изменить значение поля camera (Только SQL)\n'
                        '5 - Удалить данные в БД (Только SQL)\n'
                        '6 - Обновить поля camera и place_name (С инвентори для перенастройки сервера)\n'
                        '\n'
                        'Для работы со мной нужно загрузить актуальны файл Metro.xlsx, '
                        'в противном случае я буду использовать старые данные '
                        'после выбора одного из действий вы получите 3 файла конфигурации.\n'
                        '\n'
                        '<b>Итак! Что вы хотите?</b>',
                        reply_markup=kb_help
                        )
    # await message.delete() # раскомитить после отладки


@dp.callback_query_handler()
async def reload_file(callback: types.CallbackQuery):
    if callback.data == "PUSH_FILE":
        await callback.message.answer("Отлично, загрузите файл и нажмите кнопку применить\n"
                                      f'Последний файл был загружен <b>{file_filler}</b> <b>{last_date_load}</b>',
                                      reply_markup=kb_apply_load
                                      )
    else:
        await callback.message.answer("CREATE_CONF")


@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    file_info = await bot.get_file(message.photo[-1].file_id)
    locate = os.path.dirname(__file__)
    pwd = os.path.join(locate, 'data', '111.JPEG')
    await message.photo[-1].download(file_info.file_path.split('photos/')[1]) # ++





@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(
        "Выберите одно из предложенных действий или воспользуйтесь командой /start."
    )
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)