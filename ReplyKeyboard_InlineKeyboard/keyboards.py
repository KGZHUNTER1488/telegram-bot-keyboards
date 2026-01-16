from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Показать текст")],
        [KeyboardButton(text="Очистить экран")]
    ],
    resize_keyboard=True
)

confirm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data="confirm"),
            InlineKeyboardButton(text="Нет", callback_data="cancel")
        ]
    ]
)
