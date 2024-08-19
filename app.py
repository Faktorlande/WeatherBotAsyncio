import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from dotenv import load_dotenv, find_dotenv

from handlers.start_handler import user_router

load_dotenv(find_dotenv()) #загружаем переменные из файла.env

bot = Bot(token=os.getenv('TOKEN_BOT'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# Для версии aiogram ниже 3.7 можно использовать bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)


dp = Dispatcher()
dp.include_router(user_router)

async def main() -> None:

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())

