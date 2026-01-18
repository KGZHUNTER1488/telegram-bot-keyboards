from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_kb

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Привет! 👋 Это бот учебного центра StartUm 📚\n\n"
        "Выбери направление обучения ⬇️",
        reply_markup=main_kb
    )
