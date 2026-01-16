import asyncio
from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token
from decomorout.keyboard import keyboard

start_router = Router()

@start_router.message(CommandStart())
async def comand_start(message: types.Message):
    await message.answer('Привет', reply_markup=keyboard)

@start_router.message(Command('help'))
async def comand_help(message: types.Message):
    await message.reply('Чем могу помочь?')