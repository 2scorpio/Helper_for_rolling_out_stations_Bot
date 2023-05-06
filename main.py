import logging
from aiogram import executor, types
from config import dp
from keyboards import kb_help


# Configure logging
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    user = message.from_user # Обращаемся к пользователю
    username = user.username # Берём имя пользователя
    await message.answer(
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
                        'после выбора одного из действий вы получите 3 файла конфигурации.\n'
                        '\n'
                        'Итак! Что вы хотите?',
                        reply_markup=kb_help
                        )
    # await message.delete() # раскомитить после отладки


@dp.callback_query_handler()
async def reload_file(callback: types.CallbackQuery):
    if callback.data == "PUSH_FILE":
        await callback.message.answer("Отлично, загрузите файл")
    else:
        await callback.message.answer("Выберите действие")




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
        "Выберите одно из предложенных действий или воспользуйтесь командой /start."
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)