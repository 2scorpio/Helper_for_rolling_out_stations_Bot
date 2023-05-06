import logging
from aiogram import Bot, Dispatcher, executor, types
from config import dp
from keyboards import kb_help, kb1


# Configure logging
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user # Обращаемсяк пользователю
    username = user.username # Берём имя пользователя
    await message.reply(
                        f"Привет {username}, я могу:\n"
                        '1 - Добавить новый сервер\n'
                        '2 - Добавить камеры на действующий сервер\n'
                        '3 - Изменить значение поля place_name (Только SQL)\n'
                        '4 - Изменить значение поля camera (Только SQL)\n'
                        '5 - Удалить данные в БД (Только SQL)\n'
                        '6 - Обновить поля camera и place_name (С инвентори для перенастройки сервера)\n'
                        '\n'
                        'Для работы со мной нужно загрузить актуальны файл Metro.xlsx, '
                        'в противном случае я буду использовать старые данные '
                        'после выбора одного из действий вы получите 3 файла конфигурации.'
                        )
    await message.answer("Итак! Что вы хотите?", reply_markup=kb1)
    await message.delete()


#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Сформировать конфиги", "Обновить файл с данными"]
#     keyboard.add(*buttons)
#     await message.answer("Итак! Что вы хотите?", reply_markup=keyboard)
#

@dp.callback_query_handler()
async def reload_file(callback: types.CallbackQuery):
    if callback == 'PUSH_FILE':
        return await callback.message(text="Отлично, загрузите файл")
    await callback.message("Отлично, загрузите файл")

file_filler = '' # Тот, кто последний залил файл
# @dp.callback_query_handler(text="PUSH_FILE")
# async def reload_file(call: types.CallbackQuery):
#     """Меняем файл"""
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="Замена", callback_data="CREATE_CONF"))
#     await call.message.answer('работает', reply_markup=keyboard)
#     # await message.answer("Итак! Что вы хотите?", reply_markup=keyboard)
#     #await message.answer("Отлично, загрузите файл", reply_markup=keyboard)

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(
        "Выберите одно из предложенных действий или воспользуйтесь командой /help."
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)