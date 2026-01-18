from aiogram import Router, F
from aiogram.types import Message

from keyboards import signup_kb

router = Router()

@router.message(F.text == "📘 Арифметика")
async def arithmetic(message: Message):
    await message.answer(
        "📘 Арифметика\n"
        "Возраст: 6–9 лет\n"
        "Развитие логики и счёта 🧠",
        reply_markup=signup_kb
    )

@router.message(F.text == "📖 Русский язык")
async def russian(message: Message):
    await message.answer(
        "📖 Русский язык\n"
        "Грамматика, чтение, речь ✍️",
        reply_markup=signup_kb
    )

@router.message(F.text == "🕒 Продлёнка")
async def prodlenka(message: Message):
    await message.answer(
        "🕒 Продлёнка\n"
        "Помощь с уроками и развитие 🎨",
        reply_markup=signup_kb
    )

@router.message(F.text == "💻 Программирование")
async def programming(message: Message):
    await message.answer(
        "💻 Программирование\n"
        "Возраст: 12+\n"
        "Python и проекты 🚀",
        reply_markup=signup_kb
    )

@router.message(F.text == "🇬🇧 Английский язык")
async def english(message: Message):
    await message.answer(
        "🇬🇧 Английский язык\n"
        "Разговор и грамматика 🌍",
        reply_markup=signup_kb
    )

@router.message(F.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer(
        "📞 +я не знаю\n"
        "🕒 Пн–Сб 09:00–19:00\n"
        "👤 Администратор: тож не знаю"
    )

@router.message(F.text == "📍 Адрес")
async def address(message: Message):
    await message.answer("📍 г. ОШ, ул. Араванская")
    await message.answer_location(
        latitude=42.8746,
        longitude=74.5698
    )
