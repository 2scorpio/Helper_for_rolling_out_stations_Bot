import os
import shutil

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram import types, Bot
from tgBot.handlers.other import first_blood
from tgBot.keyboards.inline import inline_kbr_upload_new_file
from tgBot.misc.other_bot_funck import delete_inline_and_msg, delete_inline_key_only_last_msg
from tgBot.misc.states import MyFlags
from tgBot.utility.main import locate


async def mein_menu_answer(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """ Эта функция отвечает на все колбеки главного меню """
    call = callback_query.data
    print(f'Я в mein_menu_answer')
    if call == 'start_cmd_1':
        await callback_query.answer('start_cmd_1')
    if call == 'start_cmd_2':
        await callback_query.answer('start_cmd_2')
    if call == 'start_cmd_3':
        await callback_query.answer('start_cmd_3')
    if call == 'start_cmd_4':
        await callback_query.answer('start_cmd_4')
    if call == 'start_cmd_5':
        await callback_query.answer('start_cmd_5')
    if call == 'start_cmd_6':
        await callback_query.answer('start_cmd_6')
    if call == 'start_upload':
        await callback_query.message.answer('Бот ожидает загрузки файла', reply_markup=inline_kbr_upload_new_file)
        await delete_inline_and_msg(callback_query.message)  # Удаление инлай клавиатуры с предыдущего сообщения и сообщения пользователя
        await state.set_state(MyFlags.UPLOAD)  # Ставим флаг загрузки файла
    else:
        await callback_query.answer(
            'Сорри, разработчика, скорее всего, заставляют работать другую бесполезную работу, выберите пока что ни '
            'будь другое. Спасибо за понимание.',
            show_alert=True
        )


async def upload_menu_call(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """ Эта функция отвечает на все колбеки меню загрузки при включённом FSM UPLOAD """
    bot: Bot = callback_query.bot
    call = callback_query.data
    print(f'Я в upload_menu_call')
    if call == 'upload_download_reference_file':
        await delete_inline_key_only_last_msg(callback_query)
        file_ref_locate = os.path.join(locate, 'data', 'reference', 'Metro.xlsx')  # Локация файла
        if os.path.exists(file_ref_locate):
            with open(file_ref_locate, 'rb') as foo:
                await bot.send_document(callback_query.from_user.id, document=foo, caption='Вот образец, бездарь!')
        else:
            await callback_query.answer(
                'Сорри, файлик потерялся',
                show_alert=True
            )
        await callback_query.message.answer(
            'Бот ожидает загрузки файла',
            reply_markup=inline_kbr_upload_new_file
        )
    if call == 'upload_back':
        tmp_file_locate = os.path.join(locate, 'data', 'tmp', 'Metro.xlsx')
        await state.finish()
        await first_blood(callback_query.message)
        if os.path.exists(tmp_file_locate):
            os.remove(tmp_file_locate)



async def moving_file(callback_query: types.CallbackQuery, state: FSMContext):
    """ Меню приминения нового файла """
    call = callback_query.data
    print(f'Я в moving_file')
    file = os.path.join(locate, 'data', 'tmp', 'Metro.xlsx')
    destination_folder = os.path.join(locate, 'data', 'current_file', 'Metro.xlsx')
    await callback_query.answer('Готово!')
    try:
        shutil.move(file, destination_folder)
    except FileNotFoundError:
        await call.answer('Упс, сообщите разработчику, что временный файл протерялся и его обновить не удалось.', show_alert=True)
    await state.finish()
    await first_blood(callback_query.message)



def callback_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_callback_query_handler(mein_menu_answer, lambda call: call.data.startswith('start_'))
    dp.register_callback_query_handler(upload_menu_call, lambda call: call.data.startswith('upload_'), state=MyFlags.UPLOAD)
    dp.register_callback_query_handler(moving_file, lambda call: call.data == 'apply_moving_file', state=MyFlags.UPLOAD)