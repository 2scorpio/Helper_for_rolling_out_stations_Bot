from aiogram import Dispatcher

from tgBot.handlers.admin import register_admin_handlers
from tgBot.handlers.other import register_other_handlers
from tgBot.handlers.user import register_user_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_user_handlers,
        register_admin_handlers,
        register_other_handlers,
    )
    for handler in handlers:
        handler(dp)