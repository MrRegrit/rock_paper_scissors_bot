from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU

start_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['btn_start_search'])
rules_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['btn_rules'])
nick_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['btn_change_nick'])
stat_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['btn_statistic'])

off_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['btn_stop_search'])

rock_btn: KeyboardButton = KeyboardButton(text='🪨')
paper_btn: KeyboardButton = KeyboardButton(text='🧻')
scissors_btn: KeyboardButton = KeyboardButton(text='✂️')

keyboard_start_search = ReplyKeyboardMarkup(keyboard=[[start_btn], [stat_btn], [rules_btn], [nick_btn]], resize_keyboard=True)

keyboard_off_search = ReplyKeyboardMarkup(keyboard=[[off_btn]], resize_keyboard=True)

keyboard_game = ReplyKeyboardMarkup(keyboard=[[rock_btn, scissors_btn, paper_btn]], resize_keyboard=True)