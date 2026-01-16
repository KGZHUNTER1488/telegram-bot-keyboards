import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import reply_keyboard

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    logging.info("Команда /start")
    await message.answer(
        "Привет! 🤖",
        reply_markup=reply_keyboard
    )
