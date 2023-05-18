from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from tgBot.misc.states import MyFlags





# inline_kbr_upload_new_file

def messages_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    # !!!dp.register_message_handler(upload_menu, lambda call: call.data.startswith('upload_'), state=MyFlags.UPLOAD)
