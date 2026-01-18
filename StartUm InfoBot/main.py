import asyncio
import logging
from aiogram import Dispatcher

from config import bot
from start_commands import router as start_router
from menu_handlers import router as menu_router

async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    # подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(menu_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
