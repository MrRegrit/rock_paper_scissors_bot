from aiogram import Router, F, Bot
from aiogram.types import Message
from filters.filters import GameStatusFilter, PlayersMovedFilter
from aiogram.methods.send_message import SendMessage
from keyboard.keyboard import keyboard_start_search, keyboard_game

from models.models import users

router: Router = Router()

router.message.filter(GameStatusFilter())


@router.message(F.text.in_({'🪨', '✂️', '🧻'}))
async def test(message: Message, bot: Bot):
    my_id = message.from_user.id
    enemy_id = users[message.from_user.id]['enemy_id']
    users[my_id]['move'] = ['🪨', '✂️', '🧻'].index(message.text) + 1
    my_move = ['🪨', '✂️', '🧻'].index(message.text) + 1
    enemy_move = users[enemy_id]['move']
    await message.answer(f'Вы сходили: {message.text}')
    if enemy_move == 0:
        await message.answer('Ждем пока ваш соперник сходит')
        await bot.send_message(chat_id=users[my_id]['enemy_id'], text='Ваш соперник уже сходил')
    else:
        users[my_id]['move'] = 0
        users[enemy_id]['move'] = 0
        if my_move == enemy_move:
            winner = 0
        elif my_move - enemy_move == -1 or my_move - enemy_move == 2:
            winner = my_id
            users[my_id]['score'] += 1
        else:
            winner = enemy_id
            users[enemy_id]['score'] += 1

        await message.answer(f'{users[enemy_id]["nickname"]} сходил(а): {["🪨", "✂️", "🧻"][enemy_move - 1]}')
        await message.answer(f'\nОчко забирает: {users[winner]["nickname"] if winner != 0 else "никто"}'
                             f'\nСчет: {users[my_id]["score"]} / {users[enemy_id]["score"]}')
        await bot.send_message(chat_id=users[my_id]["enemy_id"],
                               text=f'{users[my_id]["nickname"]} сходила(а) {["🪨", "✂️", "🧻"][my_move - 1]}')
        await bot.send_message(chat_id=users[my_id]["enemy_id"],
                               text=f'\nОчко забирает: {users[winner]["nickname"] if winner != 0 else "никто"}'
                                    f'\nСчет: {users[enemy_id]["score"]} / {users[my_id]["score"]}')
        if users[my_id]["score"] >= 3 or users[enemy_id]["score"] >= 3:
            win_nick = users[winner]["nickname"]
            users[my_id]['game_status'] = False
            users[enemy_id]['game_status'] = False
            if users[my_id]["score"] >= 3:
                users[my_id]['wins'] += 1
            else:
                users[enemy_id]['wins'] += 1
            users[my_id]['score'] = 0
            users[enemy_id]['score'] = 0
            users[my_id]['total_games'] += 1
            users[enemy_id]['total_games'] += 1
            await message.answer(f'\n{"Игра завершена! Победитель:" + win_nick}', reply_markup=keyboard_start_search)

            await bot.send_message(chat_id=users[my_id]["enemy_id"],
                                   text=f'\n{"Игра завершена! Победитель:" + win_nick}',
                                   reply_markup=keyboard_start_search)
        else:
            await message.answer('Следующий раунд! Ходите:')
            await bot.send_message(chat_id=users[my_id]["enemy_id"], text='Следующий раунд! Ходите:')


@router.message()
async def test(message: Message):
    await message.answer(f'Пожалуйста, выберите камень, ножницы или бумагу')
