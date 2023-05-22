from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_kbr_start_menu = InlineKeyboardMarkup()
""" Клавиатура для стартового меню """
inline_kbr_start_menu.add(InlineKeyboardButton(text='1. - Добавить новый сервер'.upper(), callback_data="start_cmd_1")) # callback_data="new_server"))
inline_kbr_start_menu.add(InlineKeyboardButton(text='2. - Добавить камеры на действующий сервер'.upper(), callback_data="start_cmd_2")) # callback_data="add_cam_current_server"))
inline_kbr_start_menu.add(InlineKeyboardButton(text='3. - Изменить значение поля place_name'.upper(), callback_data="start_cmd_3")) # callback_data="change_the_server_value"))
inline_kbr_start_menu.add(InlineKeyboardButton(text='4. - Изменить значение поля camera'.upper(), callback_data="start_cmd_4")) # callback_data="change_the_camera_value"))
inline_kbr_start_menu.add(InlineKeyboardButton(text='5. - Удалить данные в БД'.upper(), callback_data="start_cmd_5")) # callback_data="delete_data_in_bd"))
inline_kbr_start_menu.add(InlineKeyboardButton(text='6. - Обновить поля camera и place_name'.upper(), callback_data="start_cmd_6")) # callback_data="update_filed_cam"))
inline_kbr_start_menu.add(InlineKeyboardButton(text="Обновить файл".upper(), callback_data="start_upload"))
inline_kbr_start_menu.add(InlineKeyboardButton(text='Справка'.upper(), callback_data="start_help"))
inline_kbr_start_menu.add(InlineKeyboardButton(text='Получить данные пользователя'.upper(), callback_data="user_data"))



inline_kbr_upload_new_file = InlineKeyboardMarkup()
""" Клавиатура меню 1го уровня меню загрузка файла """
inline_kbr_upload_new_file.add(InlineKeyboardButton(text="Скачать образец", callback_data="upload_download_reference_file"))
inline_kbr_upload_new_file.add(InlineKeyboardButton(text="Назад", callback_data="upload_back"))


inline_kbr_new_file_apply = InlineKeyboardMarkup()
""" Клавиатура меню 2го уровня меню загрузка файла """
inline_kbr_new_file_apply.add(InlineKeyboardButton(text="Применить файл", callback_data="apply_moving_file")) # callback_data="apply"))
inline_kbr_new_file_apply.add(InlineKeyboardButton(text="Оставить старый файл", callback_data="upload_back"))


