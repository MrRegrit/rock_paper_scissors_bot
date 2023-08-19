from aiogram import Router, F
from aiogram.types import Message
from filters.filters import SearchFilter

from keyboard.keyboard import keyboard_start_search

from models.models import users, queue
from lexicon.lexicon import LEXICON_RU

router: Router = Router()

router.message.filter(SearchFilter())


@router.message(F.text == LEXICON_RU['btn_stop_search'])
async def change_nick(message: Message):
    users[message.from_user.id]['search_status'] = False
    queue.remove(message.chat.id)
    await message.answer(text=f'Поиск остановлен', reply_markup=keyboard_start_search)
