from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

print("keyboards.py загружен")  # ← ДЛЯ ПРОВЕРКИ

# Главное меню
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📘 Арифметика"), KeyboardButton(text="📖 Русский язык")],
        [KeyboardButton(text="🕒 Продлёнка")],
        [KeyboardButton(text="💻 Программирование"), KeyboardButton(text="🇬🇧 Английский язык")],
        [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="📍 Адрес")]
    ],
    resize_keyboard=True
)

# Inline-кнопка "Записаться"
signup_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✍️ Записаться", url="https://t.me/admin")]
    ]
)

