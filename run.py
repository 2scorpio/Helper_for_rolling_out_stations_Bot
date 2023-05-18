from tgBot import start_bot

if __name__ == '__main__':
    start_bot()


# Пример Колбека - lambda c: c.data:
# {"id": "5522667486428702424",
#  "from": {"id": 1285846225,
#           "is_bot": false,
#           "first_name": "Артем",
#           "last_name": "Привалов",
#           "username": "tema_rrr",
#           "language_code": "ru"},
#  "message": {"message_id": 5734,
#              "from": {"id": 5893532212,
#                       "is_bot": true,
#                       "first_name": "Face_Helper_Bot",
#                       "username": "Face_Halper_Bot"},
#              "chat": {"id": 1285846225,
#                       "first_name": "Артем",
#                       "last_name": "Привалов",
#                       "username": "tema_rrr",
#                       "type": "private"},
#              "date": 1684410925,
#              "text": "Как будет действовать хацкер?\nПоследний файл был загружен [КЕМ] и [КОГДА]",
#              "reply_markup":
#                  {"inline_keyboard": [[{"text": "1. - ДОБАВИТЬ НОВЫЙ СЕРВЕР", "callback_data": "start_comm_1"}],
#                                       [{"text": "2. - ДОБАВИТЬ КАМЕРЫ НА ДЕЙСТВУЮЩИЙ СЕРВЕР", "callback_data": "start_comm_2"}],
#                                       [{"text": "3. - ИЗМЕНИТЬ ЗНАЧЕНИЕ ПОЛЯ PLACE_NAME", "callback_data": "start_comm_3"}],
#                                       [{"text": "4. - ИЗМЕНИТЬ ЗНАЧЕНИЕ ПОЛЯ CAMERA", "callback_data": "start_comm_4"}],
#                                       [{"text": "5. - УДАЛИТЬ ДАННЫЕ В БД", "callback_data": "start_comm_5"}],
#                                       [{"text": "6. - ОБНОВИТЬ ПОЛЯ CAMERA И PLACE_NAME", "callback_data": "start_comm_6"}],
#                                       [{"text": "ОБНОВИТЬ ФАЙЛ", "callback_data": "start_Upload"}],
#                                       [{"text": "СПРАВКА", "callback_data": "start_Help"}]]}},
#  "chat_instance": "5415836714898213049",
#  "data": "start_comm_2"}