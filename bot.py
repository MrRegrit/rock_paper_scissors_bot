import asyncio

from aiogram import Dispatcher, Bot
from config_data.config import load_config, Config
from handlers import user_handlers, change_nick_handlers, search_handlers, game_handlers


async def main() -> None:
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(search_handlers.router)
    dp.include_router(change_nick_handlers.router)
    dp.include_router(game_handlers.router)

    print('Апдейты очищены, начинаю поллинг')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
