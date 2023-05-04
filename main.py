import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token='5893532212:AAGZ7XlPlR7V8_OEfKP_4YniJnRL492FzHc')
dp = Dispatcher(bot)

@dp.message_handler(commands=['помощь', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
                        "Привет, я могу:\n"
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

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)