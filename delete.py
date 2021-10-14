import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import ADMINS
from keyboards.default.contact import contact_buttons
from loader import dp,db,bot
from filters import Shaxsiy,Admin
@dp.message_handler(commands='del')
async def delete_user(message:types.Message):
    ism = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=ism)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
    count = db.delete_users()
    aa = f" {message.from_user.full_name}{count}Admin"
    await bot.send_message(chat_id=ADMINS[0],text=aa)