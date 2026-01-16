from aiogram import Bot
from aiogram.types import BotCommand

BOT_TOKEN = "8552500529:AAHWQ2PdpP2hCp_S2ZD1TIEmsFGXCsoTY7I"

bot = Bot(token=BOT_TOKEN)

commands = [
    BotCommand(command="start", description="Начать")
]
