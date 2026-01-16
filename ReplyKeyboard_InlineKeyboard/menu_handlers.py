import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards import confirm_keyboard

router = Router()

@router.message(F.text == "Показать текст")
async def show_text(message: Message):
    logging.info("Кнопка: Показать текст")
    await message.answer(
        "Ты хочешь очистить экран?",
        reply_markup=confirm_keyboard
    )

@router.message(F.text == "Очистить экран")
async def clear_screen(message: Message):
    logging.info("Кнопка: Очистить экран")
    await message.answer(
        "Ты уверен?",
        reply_markup=confirm_keyboard
    )

@router.callback_query(F.data == "confirm")
async def confirm(callback: CallbackQuery):
    logging.info("Callback: confirm")
    await callback.message.edit_text("Экран очищен! 🧹")
    await callback.answer()

@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery):
    logging.info("Callback: cancel")
    await callback.message.edit_text("Действие отменено ❌")
    await callback.answer()
