from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

kb_help = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
kb_help.add(b1)

kb1 = types.InlineKeyboardMarkup()
kb1.add(types.InlineKeyboardButton(text="Сформировать конфиги", callback_data="CREATE_CONF"))
kb1.add(types.InlineKeyboardButton(text="Обновить файл с серверами", callback_data="PUSH_FILE"))
