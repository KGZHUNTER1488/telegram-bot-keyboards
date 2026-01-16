from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог авто")],
        [KeyboardButton(text="Контакты")],
        [KeyboardButton(text="О компании")]
    ],
    resize_keyboard=True
)

help_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог")],
        [KeyboardButton(text="Проверить авто")],
        [KeyboardButton(text="Контакты")]
    ],
    resize_keyboard=True
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Седаны представительского класса")],
        [KeyboardButton(text="Премиальные кроссоверы")],
        [KeyboardButton(text="Электромобили")],
        [KeyboardButton(text="Спорткары")]
    ],
    resize_keyboard=True
)
