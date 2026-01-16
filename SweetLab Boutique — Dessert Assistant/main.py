import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from start_commands import router as start_router
from menu_handlers import router as menu_router

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(menu_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
