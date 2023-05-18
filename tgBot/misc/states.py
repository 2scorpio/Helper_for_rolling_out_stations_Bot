from typing import Final

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class My_flags(StatesGroup):
    is_upload = False

