from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_apply_load = ReplyKeyboardMarkup(resize_keyboard=True)
kb_apply_load_1 = KeyboardButton('Применить')
kb_apply_load.add(kb_apply_load_1)

kb_help = InlineKeyboardMarkup()
kb_help_1 = InlineKeyboardButton(text="Сформировать конфиги",
                                 callback_data="CREATE_CONF")
kb_help_2 = InlineKeyboardButton(text="Обновить файл с серверами",
                                 callback_data="PUSH_FILE")
kb_help.add(kb_help_1, kb_help_2)

