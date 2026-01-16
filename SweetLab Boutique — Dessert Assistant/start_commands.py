from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards import main_kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в SweetLab Boutique 🍰\n"
        "Я могу отвечать только на вопросы, связанные с нашей кондитерской.\n"
        "Выберите действие с помощью кнопок ниже.",
        reply_markup=main_kb
    )
