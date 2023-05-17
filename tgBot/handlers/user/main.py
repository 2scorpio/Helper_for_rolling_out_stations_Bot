from aiogram import Dispatcher

from tgBot.handlers.user.for_message_handler import register_message_handlers


def register_user_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули """
    register_message_handlers(dp)





    """ Пример """
    # dp.register_message_handler(__start, commands=["start"])
    # dp.register_message_handler(__teh_support, content_types=["text"], text="Тех-поддержка ⚙")
    # dp.register_message_handler(__help, content_types=['text'], text="Узнать команды 📌")
    # _register_vip_handlers(dp)
    # _register_user_bot_handlers(dp)