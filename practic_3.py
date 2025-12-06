from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio
import random

bot = Bot(token='8252897904:AAGbr82yaWGFnteBmZ4aVvFkFQ570k-5Xh4')
dp = Dispatcher()

students = {
    "абдусамат": "Ученик — 3 месяца",
    "эртай": "Ученик — 1 месяц",
    "хазрет": "Ученик — 6 месяцев",
    "адилет": "Ученик — 2 месяца"
}
photos = [
    "https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=620&dpr=2&s=none&crop=none",
    "https://multi-admin.ru/mediabank_blog/11/297224/105ba0ae5ed326f2f20975ea2095c809_297224.jpg",
    "https://img.belta.by/images/storage/news/with_archive/2022/000029_1653572687_504261_big.jpg"
]


#1
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Напиши /help чтобы узнать мои команды.")


#2
@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "📌 Команды:\n"
        "/start — приветствие\n"
        "/help — список команд\n"
        "/about — о центре\n"
        "/contact — контакт преподавателя\n"
        "/location — локация центра\n"
        "/calc X Y — сложение чисел\n"
        "/repeat TEXT — повторить текст\n"
        "/info — информация о пользователе\n"
        "/len TEXT — длина текста\n")


#3
@dp.message(Command("about"))
async def about(message: Message):
    await message.answer("StartUm — учебный центр IT образования.")


#4
@dp.message(Command("contact"))
async def contact(message: Message):
    await message.reply_contact(phone_number="+996500000000", first_name="Преподаватель", last_name="StartUm")


#5
@dp.message(Command("location"))
async def location(message: Message):
    await message.reply_location(latitude=40.527803, longitude=72.794157)


#6
@dp.message()
async def handler(message: Message):
    text = message.text.lower()

    if text in students:
        await message.answer(students[text])
        return

    if text.isalpha():
        await message.answer("Такого ученика нет в базе!")
        return


#7
@dp.message(Command("calc"))
async def calc(message: Message):
    args = message.text.split()[1:]

    if len(args) != 2:
        return await message.answer("Введите два числа!")

    a, b = args

    for x in (a, b):
        for ch in x:
            if ch not in "0123456789":
                return await message.answer("Введите два числа!")

    result = float(a) + float(b)

    await message.answer(f"Результат: {result}")



#8
@dp.message(Command("repeat"))
async def repeat(message: Message):
    txt = message.text
    text = txt.replace("/repeat ", "", 1)
    await message.answer(text)


#9
@dp.message(F.text.lower() == "фото")
async def random_photo(message: Message):
    await message.reply_photo(random.choice(photos))


#10
@dp.message(F.text.lower() == "стих")
async def poem(message: Message):
    await message.answer(
        "Код писать — не просто дело,\n"
        "Но зато приходит смелость!\n"
        "Если будешь ты стараться —\n"
        "Будет круто получаться!")


#11
@dp.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')


# 12
@dp.message(Command("info"))
async def info(message: Message):
    user = message.from_user
    await message.answer(
        f"Имя: Даниел"
        f"Юзернейм: Daniel"
        f"ID: 12345"
    )


# 13
@dp.message(Command("len"))
async def text_len(message: Message):
    text = " ".join(message.text.split()[1:])
    if not text:
        await message.answer("Введите текст после команды!")
    await message.answer(f"Длина текста: {len(text)} символов")


#14
@dp.message(F.text.lower() == "привет")
async def greet_privet(message: Message):
    await message.answer("И тебе привет")

@dp.message(F.text.lower() == "салам")
async def greet_salam(message: Message):
    await message.answer("И тебе привет")

@dp.message(F.text.lower() == "ку")
async def greet_ku(message: Message):
    await message.answer("И тебе привет")

@dp.message(F.text.lower() == "здарова")
async def greet_zdarova(message: Message):
    await message.answer("И тебе привет")



#15
@dp.message(F.text.lower() == "пока")
async def bye_poka(message: Message):
    await message.answer("До связи!")

@dp.message(F.text.lower() == "бай")
async def bye_bai(message: Message):
    await message.answer("До связи!")

@dp.message(F.text.lower() == "до встречи")
async def bye_do_vstrechi(message: Message):
    await message.answer("До связи!")


async def main():
    await dp.start_polling(bot)

asyncio.run(main())