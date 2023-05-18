from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from tgBot.keyboards.inline import inline_kbr_upload_new_file
from tgBot.misc.states import My_flags

# todo: При передачи FSMContext зависает
async def mein_menu_answer(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """ Эта функция отвечает на все колбеки главного меню """
    call = callback_query.data
    print(call)
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
        await callback_query.message.edit_reply_markup()  # Удаляет клавиатуру при нажатии
    else:
        await callback_query.answer('Сорри, разработчика, скорее всего, заставляют работать другую бесполезную работу, выберите пока что ни будь другое. Спасибо за понимание.', show_alert=True)


def callback_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_callback_query_handler(mein_menu_answer, lambda call: call.data.startswith('start_'), state=My_flags)
