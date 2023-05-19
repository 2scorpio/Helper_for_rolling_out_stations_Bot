from aiogram import Dispatcher
from tgBot.handlers.user.for_callback_query_handler import callback_handlers
from tgBot.handlers.user.for_message_handler import messages_handlers


def register_user_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    # region
    callback_handlers(dp)
    messages_handlers(dp)
    # local
    # dp.register_message_handler(first_blood, commands=['8'], content_types=['text'], text="8")

