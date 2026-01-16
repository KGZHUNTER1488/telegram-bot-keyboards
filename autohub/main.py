from aiogram import Bot, Dispatcher
import asyncio
from config import BOT_TOKEN
from start_commands import router as start_router
from menu_handlers import router as menu_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(menu_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
