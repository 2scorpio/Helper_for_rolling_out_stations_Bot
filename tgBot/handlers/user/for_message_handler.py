import os

from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from tgBot.utility.main import locate
from tgBot.misc.other_bot_funck import delete_message_only, delete_inline_key_only_first_msg
from tgBot.misc.states import MyFlags
from tgBot.keyboards.inline import inline_kbr_upload_new_file, inline_kbr_new_file_apply


async def upload_menu_msg(msg: types.Message, state: FSMContext) -> None:
    """ Эта функция слушает документы, когда флаг загрузки включён и удаляет остальные сообщения """
    bot: Bot = msg.bot
    call = msg.date
    msg = msg
    print(f'Я в upload_menu_msg')
    if msg.document.mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        file_id = msg.document.file_id
        file_name = 'Metro.xlsx'  # Переопределяем имя
        file_path = await bot.get_file(file_id)  # Скачиваем файл
        downloaded_file = await bot.download_file(file_path.file_path)
        file = os.path.join(locate, 'data', 'tmp', file_name)
        with open(file, 'wb') as foo:
            foo.write(downloaded_file.read())
        await delete_inline_key_only_first_msg(msg)
        await msg.answer('Файл успешно загружен, выберите действие.', reply_markup=inline_kbr_new_file_apply)
    elif msg.document.mime_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        await msg.answer('Не верный формат, загрузите файл в формате XLSX.', reply_markup=inline_kbr_new_file_apply)
        await delete_message_only(msg)  # удаляет сообщение от пользователя
# todo: допилить удаление сообщений


def messages_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(upload_menu_msg, content_types=types.ContentTypes.ANY, state=MyFlags.UPLOAD)
