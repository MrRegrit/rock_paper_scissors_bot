from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, or_f
from lexicon.lexicon import LEXICON_RU
from services.services import User, get_statistics_text
from filters.filters import NotInGame
from keyboard.keyboard import keyboard_start_search, ReplyKeyboardRemove, keyboard_off_search, keyboard_game
from models.models import users, queue
from aiogram.methods.send_message import SendMessage

router: Router = Router()

router.message.filter(NotInGame())


@router.message(CommandStart())
async def process_start_command(message: Message):
    if not User.in_data(message.chat.id):
        User.add(message.chat.id, message.from_user.first_name)
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard_start_search)
    await message.answer(text=f'Сейчас ваш никнейм: {users[message.chat.id]["nickname"]}')


@router.message(or_f(Command(commands='help'), F.text == LEXICON_RU['btn_rules']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(or_f(Command(commands='nickname'), F.text == LEXICON_RU['btn_change_nick']))
async def process_settings_command(message: Message):
    users[message.chat.id]['change_nick'] = True
    await message.answer(text=LEXICON_RU['/nickname'], reply_markup=ReplyKeyboardRemove())


@router.message(or_f(Command(commands='statistics'), F.text == LEXICON_RU['btn_statistic']))
async def process_statisticks_command(message: Message):
    await message.answer(text=get_statistics_text(message.chat.id, LEXICON_RU['/statistics']))


@router.message(F.text == LEXICON_RU['btn_start_search'])
async def find_enemy(message: Message, bot: Bot):
    users[message.from_user.id]['search_status'] = True
    await message.answer(text='Поиск начат')
    if len(queue) == 0:
        await message.answer(
            text=f'В поиске пока никого нет :(',
            reply_markup=keyboard_off_search)
        queue.append(message.from_user.id)
    else:
        await message.answer(text=f'Игрок найден!\nВаш соперник: {users[queue[0]]["nickname"]}')
        await message.answer(text=f'Игра начинается! Выбирайте:', reply_markup=keyboard_game)
        users[message.chat.id]['game_status'] = True
        users[queue[0]]['game_status'] = True
        users[message.chat.id]['search_status'] = False
        users[queue[0]]['search_status'] = False
        users[message.chat.id]['enemy_id'] = queue[0]
        users[queue[0]]['enemy_id'] = message.chat.id
        chat_id = queue[0]
        queue.pop(0)
        await bot.send_message(chat_id=chat_id, text=f'Игрок найден!'
                                                    f'\nВаш соперник: {users[message.chat.id]["nickname"]}')
        await bot.send_message(chat_id=chat_id, text=f'Игра начинается! Выбирайте:', reply_markup=keyboard_game)
