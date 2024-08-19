from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
import os


from handlers.menu_processing import get_menu_content

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    #media, reply_markup = await get_menu_content(level=0, menu_name='main')
    #file_id = 'AgACAgIAAxkDAAMvZsIQo1V5THd8haBWP7uO1vrweoQAAn7kMRt93xFKR6x8CDeNPNsBAAMCAANzAAM1BA'
    # with open('banners/main_menu_summer1.jpg', 'rb') as file:
    #     r = requests.post(f'https://api.telegram.org/bot{os.getenv("TOKEN_BOT")}/sendPhoto',
    #                       data={'chat_id': message.chat.id},
    #                       files={"photo": file})
    # data = dict(r.json())
    # file_id = data['result']['photo'][0]['file_id']
    # print(file_id)
    #await message.answer("Привет! Я бот, который поможет тебе запланировать день.\nНу и одеться по погоде))")
    # await message.answer_photo(photo=file_id,
    #                            caption="Привет! Я бот, который поможет тебе запланировать день.\nНу и одеться по погоде))"
    #                            )
    media, reply_markup = await get_menu_content(level=0, menu_name='main')
    await message.answer_photo(media, reply_markup=reply_markup)















