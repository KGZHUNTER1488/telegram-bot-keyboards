from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio

bot = Bot(token='8591872632:AAGbJ8-A03iIIrt5fY7--BaKzBt-Q5cHsl8')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Привет лысый!')

@dp.message(Command('help'))
async def help(message:Message):
    await message.reply('Чем могу помочь?')

@dp.message(Command('about'))
async def about(message: Message):
    await message.reply('Startum - это учебный центр в городе Ош')

@dp.message(Command('contact'))
async def contact(message: Message):
    await message.reply_contact(phone_number='+996500273979', last_name='Nuraziz', first_name='Makyev')

@dp.message(Command('location'))
async def location(message:Message):
    await message.reply_location(latitude=40.527803, longitude=72.794157)
    
@dp.message(F.text.lower() == 'абдусамат')
async def abdusamat(message:Message):
    await message.reply('Ученик - 3 месяца')

@dp.message(F.text.lower() == 'фото')
async def photo(message:Message):
    await message.reply_photo(photo='https://multi-admin.ru/mediabank_blog/11/297224/105ba0ae5ed326f2f20975ea2095c809_297224.jpg')

@dp.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')

@dp.message(F.text.lower() == 'стикер')
async def stiker(message:Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAAMPaSfL5dXU-_WP6UGcnHlSAk2NdiQAAodWAAJqrXFLw2G_LcVtFgABNgQ')

async def main():
    await dp.start_polling(bot)

asyncio.run(main())