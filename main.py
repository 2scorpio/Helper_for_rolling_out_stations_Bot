import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token='5893532212:AAGZ7XlPlR7V8_OEfKP_4YniJnRL492FzHc')
dp = Dispatcher(bot)

### Face_Halper_Bot

@dp.message_handler(commands=['помощь', 'help', 'start', 'го'])
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
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Сформировать конфиги", callback_data="random_value"))
    keyboard.add(types.InlineKeyboardButton(text="Обновить файл с серверами", callback_data="random_value"))
    await message.answer("Итак! Что вы хотите?", reply_markup=keyboard)


#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Сформировать конфиги", "Обновить файл с данными"]
#     keyboard.add(*buttons)
#     await message.answer("Итак! Что вы хотите?", reply_markup=keyboard)
#
# @dp.message_handler(commands='g')
# async def cmd_random(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
#     await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(
        "Выберите одно из предложенных действий или воспользуйтесь командой /help."
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)