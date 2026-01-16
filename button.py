import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token

bot = Bot(token=token)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='меню'), KeyboardButton(text='контакты')]
    [KeyboardButton(text='о нас')]
]

keybord = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку', one_time_keyboard=True)

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Превое'), KeyboardButton(text='Второе'), KeyboardButton(text='Третье')],
    [KeyboardButton(text='Фастфуд'), KeyboardButton(text='Напитки'), KeyboardButton(text='Салаты')]
], resize_keyboard=True, input_field_placeholder=True, one_time_keyboard=True)

@dp.message(CommandStart())
async def comand_start(message: types.Message):
    await message.answer('Привет', reply_markup=keybord)

@dp.message(Command('help'))
async def comand_help(message: types.Message):
    await message.reply('Чем могу помочь?')

@dp.message(F.text == 'меню')
async def command_menu(message: types.Message):
    await message.answer_photo(photo='https://multi-admin.ru/mediabank_blog/11/297224/105ba0ae5ed326f2f20975ea2095c809_297224.jpg', reply_markup=menu_keyboard)

@dp.message(F.text.in_({'привет', 'првет'}))
async def command_help(message: types.Message):
    await message.reply('Привет')

@dp.message()
async def echo(message: types.Message):
    await message.answer('я вас не понял')

async def main():
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Выход')