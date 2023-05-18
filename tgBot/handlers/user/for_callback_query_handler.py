from aiogram import Dispatcher, types
from aiogram.bot import bot
from aiogram.dispatcher import FSMContext

from aiogram import Bot, types


from tgBot.keyboards.inline import inline_kbr_upload_new_file, inline_kbr_start_menu
from tgBot.misc.states import MyFlags
from tgBot.misc.other_bot_funck import delete_inline_and_msg, delete_inline_and_msg
from tgBot.misc.text_messages import start_menu_massage


async def mein_menu_answer(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """ Эта функция отвечает на все колбеки главного меню """
    call = callback_query.data
    print(f'Я в {call}')
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
            'Сорри, разработчика, скорее всего, заставляют работать другую бесполезную работу, выберите пока что ни будь другое. Спасибо за понимание.',
            show_alert=True)


async def upload_menu(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """ Эта функция отвечает на все колбеки меню загрузки при включённом FSM UPLOAD """
    call = callback_query.data
    print(f'Я в {call}')
    if call == 'upload_download_reference_file':
        await callback_query.answer('upload_download_reference_file')
    if call == 'upload_Back':
        await state.finish()
        # await first_blood(callback_query.message)
        await delete_inline_and_msg(callback_query.message)  # Удаление инлай клавиатуры с предыдущего сообщения и сообщения пользователя
        await callback_query.message.answer(text=start_menu_massage, reply_markup=inline_kbr_start_menu)
    else:
        await state.finish()
        await callback_query.message.delete()  # удаляет предыдущее сообщение пользователя
        await delete_inline_and_msg(callback_query.message)


def callback_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_callback_query_handler(mein_menu_answer, lambda call: call.data.startswith('start_'))
    dp.register_callback_query_handler(upload_menu, lambda call: call.data.startswith('upload_'), state=MyFlags.UPLOAD)
