from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from keyboards import *
from config import prices, allowed_words
import random

router = Router()

PHOTOS = {
    "🎂 Торты": "photos/cakes.jpg",
    "🍬 Макаруны": "photos/macarons.jpg",
    "🍮 Пирожные": "photos/desserts.jpg",
    "🥗 Без сахара": "photos/sugarfree.jpg",
    "⭐ Хиты продаж": "photos/hits.jpg"
}

@router.message(F.text == "🍰 Каталог")
async def catalog(message: Message):
    await message.answer("Выберите категорию десертов:", reply_markup=catalog_kb)

@router.message(F.text.in_(PHOTOS.keys()))
async def category(message: Message):
    photo = FSInputFile(PHOTOS[message.text])
    await message.answer_photo(
        photo=photo,
        caption="Наши десерты 🍰",
        reply_markup=category_kb
    )

@router.message(F.text == "💰 Цены")
async def price_info(message: Message):
    await message.answer(
        "Чтобы узнать цену, напишите:\nцена <название десерта>"
    )

@router.message(F.text.lower().startswith("цена"))
async def price_check(message: Message):
    parts = message.text.lower().split(maxsplit=1)
    if len(parts) < 2:
        await message.answer("Используйте формат: цена <название>")
        return

    name = parts[1]
    if name in prices:
        await message.answer(f"Цена «{name.capitalize()}»: {prices[name]} сом")
    else:
        await message.answer("Такого десерта нет в нашем каталоге 🍰")

@router.message(F.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer(
        "Вы можете оставить номер телефона:",
        reply_markup=contact_kb
    )

@router.message(F.contact)
async def get_contact(message: Message):
    await message.answer(
        "Спасибо! Мы свяжемся с вами в ближайшее время.",
        reply_markup=main_kb
    )

@router.message(F.text == "📍 Адрес")
async def address(message: Message):
    await message.answer_location(42.8746, 74.5698)
    await message.answer("Мы ждём вас по этому адресу 🍰")

@router.message(F.text == "ℹ О студии")
async def about(message: Message):
    await message.answer(
        "SweetLab Boutique — кондитерская студия премиум-класса.\n"
        "Работаем с 2018 года."
    )

@router.message(F.text == "⬅ Главное меню")
async def back_to_menu(message: Message):
    await message.answer("Главное меню:", reply_markup=main_kb)

@router.message(F.sticker)
async def sticker(message: Message):
    await message.answer(message.sticker.file_id)

@router.message()
async def fallback(message: Message):
    text = message.text.lower()
    if not any(word in text for word in allowed_words):
        await message.answer(
            "Я могу отвечать только на вопросы, связанные с нашей кондитерской 🍰\n"
            "Пожалуйста, используйте кнопки меню."
        )
