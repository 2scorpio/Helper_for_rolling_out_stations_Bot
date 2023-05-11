from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


##################################
kb_apply_load1 = InlineKeyboardMarkup()
kb_apply_load1.add(InlineKeyboardButton(text="Назад", callback_data="back"))
kb_apply_load1.add(InlineKeyboardButton(text="Скачать образец", callback_data="download_reference_file"))


kb_apply_load2 = InlineKeyboardMarkup()
kb_apply_load2.add(InlineKeyboardButton(text="Применить файл", callback_data="4444")) # callback_data="apply"))
kb_apply_load2.add(InlineKeyboardButton(text="Оставить старый файл", callback_data="back"))
##################################

##################################
in_kb_help = InlineKeyboardMarkup()
in_kb_help.add(InlineKeyboardButton(text="Сформировать конфиги", callback_data="CREATE_CONF"))
in_kb_help.add(InlineKeyboardButton(text="Обновить файл с серверами", callback_data="PUSH_FILE"))
##################################

##################################
in_kb_create_conf = InlineKeyboardMarkup()
in_kb_create_conf.add(InlineKeyboardButton(text='1 - Добавить новый сервер', callback_data="4444")) # callback_data="new_server"))
in_kb_create_conf.add(InlineKeyboardButton(text='2 - Добавить камеры на действующий сервер', callback_data="4444")) # callback_data="add_cam_current_server"))
in_kb_create_conf.add(InlineKeyboardButton(text='3 - Изменить значение поля place_name (Только SQL)', callback_data="4444")) # callback_data="change_the_server_value"))
in_kb_create_conf.add(InlineKeyboardButton(text='4 - Изменить значение поля camera (Только SQL)', callback_data="4444")) # callback_data="change_the_camera_value"))
in_kb_create_conf.add(InlineKeyboardButton(text='5 - Удалить данные в БД (Только SQL)', callback_data="4444")) # callback_data="delete_data_in_bd"))
in_kb_create_conf.add(InlineKeyboardButton(text='6 - Обновить поля camera и place_name (С инвентори для перенастройки сервера', callback_data="4444")) # callback_data="update_filed_cam"))
in_kb_create_conf.add(InlineKeyboardButton(text='Назад', callback_data="back"))


##################################
