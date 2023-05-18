from aiogram import Dispatcher
from aiogram.types import Message
from tgBot.handlers.user.for_callback_query_handler import callback_handlers
from tgBot.keyboards.inline import inline_kbr_start_menu
from tgBot.misc.other_bot_funck import delete_inline_button_in_message_handler
from tgBot.misc.text_messages import start_menu_massage


async def first_blood(msg: Message) -> None:
    """ Функция для 1‑го запуска """
    print("Я в first_blood")
    await msg.delete()  # удаляет предыдущее сообщение пользователя
    await delete_inline_button_in_message_handler(msg) # Удаление инлай клавиатуры с предыдущего сообщения для message_handler
    await msg.answer(start_menu_massage, reply_markup=inline_kbr_start_menu)



def register_user_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    # region
    callback_handlers(dp)

    # local
    dp.register_message_handler(first_blood, commands=['8'], content_types=['text'], text="8")

