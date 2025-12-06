from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio

bot = Bot(token='8338187977:AAF9ooAS3TnnE5EgYLwwIBlUnz6h1eznda8')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Привет лысый!')

#1
@dp.message(Command('name'))
async def name(message:Message):
    await message.reply('Меня зовут Азамат')

#2
@dp.message(Command('city'))
async def city(message:Message):
    await message.reply_location(latitude=40.517575, longitude=72.805411)

#3
@dp.message(F.text.lower() == 'привет')
async def hello(messege:Message):
    await messege.reply('Привет, как дела?')

#4
@dp.message(F.text.lower() == 'пока')
async def goodbay(messege:Message):
    await messege.reply('До встречи!')

#5
@dp.message(Command('mycontact'))
async def mycontact(message: Message):
    await message.reply_contact(phone_number='+996505861189', last_name='Daniel', first_name='Asanov')
    
#6
@dp.message(Command('myphoto'))
async def photo(message:Message):
    await message.reply_photo(photo='https://multi-admin.ru/mediabank_blog/11/297224/105ba0ae5ed326f2f20975ea2095c809_297224.jpg')
    
#7
@dp.message(Command('mylocation'))
async def location(message:Message):
    await message.reply_location(latitude=40.527803, longitude=72.794157)

#8
@dp.message(F.text.lower() == 'кот')
async def catphoto(message:Message):
    await message.reply_photo(photo='https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=620&dpr=2&s=none&crop=none')

#9
@dp.message(F.text.lower() == 'стик')
async def stiker(message:Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAAMPaSfL5dXU-_WP6UGcnHlSAk2NdiQAAodWAAJqrXFLw2G_LcVtFgABNgQ')

#10
@dp.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')

#11
@dp.message(F.text.lower() == 'как дела?')
async def howareyou(message:Message):
    await message.reply('У меня всё отлично! А у тебя?')

#12
@dp.message(Command('startum'))
async def startum(message:Message):
    await message.reply('Startum - это учебный центр в городе Ош')
    await message.reply_photo(photo='https://multi-admin.ru/mediabank_blog/11/297224/105ba0ae5ed326f2f20975ea2095c809_297224.jpg')
    await message.reply_location(latitude=40.527803, longitude=72.794157)

#13
@dp.message(F.text.lower() == 'погода')
async def wether(message:Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAAMPaSfL5dXU-_WP6UGcnHlSAk2NdiQAAodWAAJqrXFLw2G_LcVtFgABNgQ') #у меня нет стикера спогодой такчто друго поставил

#14 нету там в задании его просто нет сами посмотрите

#15
@dp.message(Command('info'))
async def startum(message:Message):
    await message.reply('Имя - Даниел')
    await message.reply('Гопод - Ош')
    await message.reply('Возраст - 14')

#16
@dp.message(Command('profile'))
async def profile(message:Message):
    await message.reply_contact(phone_number='+996505861189', last_name='Daniel', first_name='Asanov')
    await message.reply_photo(photo='https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=620&dpr=2&s=none&crop=none')
    await message.reply_location(latitude=40.527803, longitude=72.794157)
    await message.reply_sticker(sticker='CAACAgIAAxkBAAMPaSfL5dXU-_WP6UGcnHlSAk2NdiQAAodWAAJqrXFLw2G_LcVtFgABNgQ')

#17
@dp.message(F.text.lower() == 'меню')
async def menu(message:Message):
    await message.reply_photo(photo='https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=620&dpr=2&s=none&crop=none')
    await message.reply_location(latitude=40.527803, longitude=72.794157)
    await message.reply_contact(phone_number='+996505861189', last_name='Daniel', first_name='Asanov')
    await message.reply_sticker(sticker='CAACAgIAAxkBAAMPaSfL5dXU-_WP6UGcnHlSAk2NdiQAAodWAAJqrXFLw2G_LcVtFgABNgQ')

#18
@dp.message()
async def unknown(message:Message):
    await message.answer("Я не понимаю, напиши /help чтобы узнать команды.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
