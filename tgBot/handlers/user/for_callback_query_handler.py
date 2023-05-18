from aiogram import Dispatcher, types


async def mein_menu_answer(callback_query: types.CallbackQuery):
    """ Эта функция отвечает на все колбеки главного меню """
    call = callback_query.data
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
    else:
        """ Заглушка """
        await callback_query.answer('Сорри, разработчика, скорее всего, заставляют работать другую бесполезную работу, выберите пока что ни будь другое. Спасибо за понимание.', show_alert=True)



def callback_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_callback_query_handler(mein_menu_answer, lambda call: call.data.startswith('start_'))
