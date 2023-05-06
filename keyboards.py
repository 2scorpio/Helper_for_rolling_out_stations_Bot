#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
# b1 = KeyboardButton('/help')
# kb1.add(b1)

kb_help = InlineKeyboardMarkup()
kb_help_1 = InlineKeyboardButton(text="Сформировать конфиги",
                                 callback_data="CREATE_CONF")
kb_help_2 = InlineKeyboardButton(text="Обновить файл с серверами",
                                 callback_data="PUSH_FILE")
kb_help.add(kb_help_1, kb_help_2)

