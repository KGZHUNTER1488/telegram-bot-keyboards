from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍰 Каталог"),
            KeyboardButton(text="💰 Цены")
        ],
        [
            KeyboardButton(text="🛒 Оформить заказ")
        ],
        [
            KeyboardButton(text="📞 Контакты"),
            KeyboardButton(text="📍 Адрес")
        ],
        [
            KeyboardButton(text="ℹ О студии")
        ]
    ],
    resize_keyboard=True
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎂 Торты"),
            KeyboardButton(text="🍬 Макаруны")
        ],
        [
            KeyboardButton(text="🍮 Пирожные"),
            KeyboardButton(text="🥗 Без сахара")
        ],
        [
            KeyboardButton(text="⭐ Хиты продаж")
        ],
        [
            KeyboardButton(text="⬅ Главное меню")
        ]
    ],
    resize_keyboard=True
)

category_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💰 Узнать цену"),
            KeyboardButton(text="📸 Показать фото")
        ],
        [
            KeyboardButton(text="🛒 Заказать")
        ],
        [
            KeyboardButton(text="⬅ Назад")
        ]
    ],
    resize_keyboard=True
)

contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📲 Отправить номер",
                request_contact=True
            )
        ],
        [
            KeyboardButton(text="⬅ Главное меню")
        ]
    ],
    resize_keyboard=True
)
