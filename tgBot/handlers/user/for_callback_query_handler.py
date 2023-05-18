from aiogram import Dispatcher, types


async def mein_menu_answer(call: types.CallbackQuery):
    call = call.data

    print('Я в mein_menu_answer')
    print(call)
    # """ Эта функция отвечает на все колбеки главного меню """
    # if call == 'start_cmd_1':
    #     await call.answer('Вы выбрали Callback 1')
    # if call == 'start_cmd_2':
    #     await call.answer('Вы выбрали Callback 2')
    # if call == 'start_cmd_3':
    #     await call.answer('Вы выбрали Callback 3')
    # if call == 'start_cmd_4':
    #     await call.answer('Вы выбрали Callback 4')
    # if call == 'start_cmd_5':
    #     await call.answer('Вы выбрали Callback 5')
    # if call == 'start_cmd_6':
    #     await call.answer('Вы выбрали Callback 6')
    #


def register_callback_handlers(dp: Dispatcher) -> None:
    """ Регистрируем модули или функции """
    dp.register_callback_query_handler(mein_menu_answer, lambda call: call.data)
