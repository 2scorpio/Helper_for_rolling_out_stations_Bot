from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from tgBot.misc.text_messages import start_menu_massage
from tgBot.utility.main import *
from tgBot.misc.other_bot_funck import delete_inline_key_only_first_msg, delete_inline_and_msg
from tgBot.misc.states import MyFlags
from tgBot.keyboards.inline import inline_kbr_upload_new_file, inline_kbr_new_file_apply, inline_kbr_start_menu


async def upload_menu_msg(msg: types.Message, state: FSMContext) -> None:
    """ Эта функция слушает документы, когда флаг загрузки включён и удаляет остальные сообщения """
    bot: Bot = msg.bot
    if msg.document:
        if msg.document.mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            file_id = msg.document.file_id
            file_name = 'Metro.xlsx'  # Переопределяем имя
            file_path = await bot.get_file(file_id)  # Скачиваем файл
            downloaded_file = await bot.download_file(file_path.file_path)
            file = os.path.join(locate_tgbot_utility_data_current_file, file_name)
            with open(file, 'wb') as foo:
                foo.write(downloaded_file.read())
            await delete_inline_key_only_first_msg(msg)
            await bot.send_message(chat_id=msg.chat.id,text='Готово, файл загружен!', reply_to_message_id=msg.message_id)
            await state.finish()
            await msg.answer(start_menu_massage, reply_markup=inline_kbr_start_menu)
        else:
            await msg.answer('Не верный формат, загрузите файл в формате XLSX.', reply_markup=inline_kbr_upload_new_file)
            await delete_inline_and_msg(msg)  # удаляет сообщение от пользователя
    else:
        await delete_inline_and_msg(msg)  # удаляет сообщение от пользователяm
        await msg.answer(
            'Бот ожидает загрузки файла.',
            reply_markup=inline_kbr_upload_new_file
        )


def messages_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_message_handler(upload_menu_msg, content_types=types.ContentTypes.ANY, state=MyFlags.UPLOAD)
