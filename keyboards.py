from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


##################################
kb_apply_load = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_apply_load_1 = KeyboardButton('Применить')
kb_apply_load_2 = KeyboardButton('Назад')
kb_apply_load.add(kb_apply_load_1, kb_apply_load_2)
##################################

##################################
in_kb_help = InlineKeyboardMarkup()
in_kb_help.add(InlineKeyboardButton(text="Сформировать конфиги", callback_data="CREATE_CONF"))
in_kb_help.add(InlineKeyboardButton(text="Обновить файл с серверами", callback_data="PUSH_FILE"))
##################################

##################################
in_kb_create_conf = InlineKeyboardMarkup()
in_kb_create_conf.add(InlineKeyboardButton(text='1 - Добавить новый сервер', callback_data="new_server"))
in_kb_create_conf.add(InlineKeyboardButton(text='2 - Добавить камеры на действующий сервер', callback_data="add_cam_current_server"))
in_kb_create_conf.add(InlineKeyboardButton(text='3 - Изменить значение поля place_name (Только SQL)', callback_data="change_the_server_value"))
in_kb_create_conf.add(InlineKeyboardButton(text='4 - Изменить значение поля camera (Только SQL)', callback_data="change_the_camera_value"))
in_kb_create_conf.add(InlineKeyboardButton(text='5 - Удалить данные в БД (Только SQL)', callback_data="delete_data_in_bd"))
in_kb_create_conf.add(InlineKeyboardButton(text='6 - Обновить поля camera и place_name (С инвентори для перенастройки сервера', callback_data="update_filed_cam"))
in_kb_create_conf.add(InlineKeyboardButton(text='Назад', callback_data="back"))


##################################
