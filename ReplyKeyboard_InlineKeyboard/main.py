import asyncio
import logging

from aiogram import Dispatcher
from config import bot, commands
import start_commands
import menu_handlers

logging.basicConfig(level=logging.INFO)

async def main():
    dp = Dispatcher()

    dp.include_router(start_commands.router)
    dp.include_router(menu_handlers.router)

    await bot.set_my_commands(commands)

    print("БОТ ЗАПУЩЕН")

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(e)
        print("Выход")

if __name__ == "__main__":
    asyncio.run(main())
