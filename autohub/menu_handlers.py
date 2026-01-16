from aiogram import Router, F
from aiogram.types import Message
from keyboards import catalog_kb
from config import prices, clients, sedans, crossovers, electro, sportcars

router = Router()

@router.message(F.text.in_({"Каталог", "Каталог авто"}))
async def catalog(message: Message):
    await message.answer(
        "Выберите категорию автомобилей:",
        reply_markup=catalog_kb
    )

@router.message(F.text == "О компании")
async def about_company(message: Message):
    await message.answer(
        "AutoHub Premium — салон люксовых автомобилей.\n"
        "Работаем с эксклюзивными авто и индивидуальными заказами."
    )

@router.message(F.text == "Контакты")
async def contacts(message: Message):
    await message.answer(
        "📞 Телефон: не скажу\n"
        "📍 Город: где-то\n"
        "🕒 Работаем 24/7"
    )

@router.message(F.text == "Седаны представительского класса")
async def sedans_handler(message: Message):
    for car in sedans:
        await message.answer_photo(car["photo"])
        await message.answer(car["name"])

@router.message(F.text == "Премиальные кроссоверы")
async def crossovers_handler(message: Message):
    for car in crossovers:
        await message.answer_photo(car["photo"])
        await message.answer(car["name"])

@router.message(F.text == "Электромобили")
async def electro_handler(message: Message):
    for car in electro:
        await message.answer_photo(car["photo"])
        await message.answer(car["name"])

@router.message(F.text == "Спорткары")
async def sportcars_handler(message: Message):
    for car in sportcars:
        await message.answer_photo(car["photo"])
        await message.answer(car["name"])

@router.message(F.text.lower().startswith("цена"))
async def price(message: Message):
    model = message.text.lower().split()[-1]
    if model in prices:
        await message.answer(f"Цена: {prices[model]:,}$")
    else:
        await message.answer("Модель не найдена.")

@router.message(F.text)
async def check_client(message: Message):
    text = message.text.lower()
    if text in clients:
        await message.answer(clients[text])
    elif not text.startswith("/"):
        await message.answer("Команда не распознана.")