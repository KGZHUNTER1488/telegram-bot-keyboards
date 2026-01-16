from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import main_menu_kb, help_kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в премиальный автосалон AutoHub Premium!\nВыберите интересующий раздел ниже.",
        reply_markup=main_menu_kb
    )

@router.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer(
        "Чем могу помочь? Выберите действие:",
        reply_markup=help_kb
    )
