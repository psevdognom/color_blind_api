

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from .loader import dp
from .messages import MESSAGES
from auth import TOKEN




class FlightsTimetableUserStates(Helper):
    mode = HelperMode.snake_case

    UNREGISTER = ListItem()
    ON_TRACK = ListItem()


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply(MESSAGES['start'])
    await message.reply_markup()



@dp.message_handler(state=FlightsTimetableUserStates.ON_TRACK)
async def renew_info(message: types.Message):

    pass