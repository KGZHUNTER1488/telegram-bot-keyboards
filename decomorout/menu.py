from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_router = Router()

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Превое'), KeyboardButton(text='Второе'), KeyboardButton(text='Третье')],
    [KeyboardButton(text='Фастфуд'), KeyboardButton(text='Напитки'), KeyboardButton(text='Салаты')]
], resize_keyboard=True, input_field_placeholder='Выберите опцию', one_time_keyboard=True)

@menu_router.message(F.text == 'меню')
async def command_help(message: types.Message):
    await message.answer_photo(photo='https://multi-admin.ru/mediabank_blog/11/297224/105ba0ae5ed326f2f20975ea2095c809_297224.jpg', reply_markup=menu_keyboard)

@menu_router.message(F.text == 'котетакты')
async def contacts(message: types.Message):
    await message.answer('Наши контакты: +996 XXX XXX XXX')

@menu_router.message(F.text.lower() == 'о нас')
async def about(message: types.Message):
    await message.answer('Мы молодая компания которая делает крутые проекты!')

@menu_router.message(F.text.in_({'привет', 'првет'}))
async def command_help(message: types.Message):
    await message.reply('Привет')