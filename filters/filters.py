from aiogram.types import Message
from aiogram.filters import BaseFilter
from models.models import users


class NotInGame(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.from_user.id not in users:
            return True
        if not users[message.from_user.id]['game_status']:
            if not users[message.from_user.id]['change_nick']:
                return True
        return False


class ChangeNickFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return users[message.from_user.id]['change_nick']


class SearchFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return users[message.from_user.id]['search_status']


class GameStatusFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return users[message.from_user.id]['game_status']


class PlayersMovedFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return users[message.from_user.id]['move'] != 0 and users[users[message.from_user.id]['enemy_id']]['move'] != 0