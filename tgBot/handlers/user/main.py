from aiogram import Dispatcher


from aiogram.types import Message
from tgBot.keyboards.inline import inline_kbr_start_menu
from tgBot.misc.text_for_messages import start_massage



async def first_blood(msg: Message) -> None:
    """ Функция для 1‑го запуска """
    await msg.answer(start_massage, reply_markup=inline_kbr_start_menu)
    #if flag_Main_menu:
        #flag_Main_menu = True

    # await delete_inline_button_in_message_handler(msg) # Добавить позже
    # await upload_flag_off() # Добавить позже
    # await msg.delete()  # удаляет предыдущее сообщение пользователя



def register_user_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(first_blood, commands=['start'])
    dp.register_message_handler(first_blood, content_types=["text"], text="start")


    """ Пример """
    # dp.register_message_handler(__start, commands=["start"])
    # dp.register_message_handler(__teh_support, content_types=["text"], text="Тех-поддержка ⚙")
    # dp.register_message_handler(__help, content_types=['text'], text="Узнать команды 📌")
    # _register_vip_handlers(dp)
    # _register_user_bot_handlers(dp)