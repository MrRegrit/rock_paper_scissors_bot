from aiogram import Router, F
from aiogram.types import Message
from filters.filters import ChangeNickFilter

from keyboard.keyboard import keyboard_start_search

from models.models import users

router: Router = Router()

router.message.filter(ChangeNickFilter())


@router.message(F.content_type == 'text')
async def change_nick(message: Message):
    users[message.chat.id]['nickname'] = message.text
    users[message.chat.id]['change_nick'] = False
    await message.answer(text=f'Ваш ник теперь: {message.text}', reply_markup=keyboard_start_search)