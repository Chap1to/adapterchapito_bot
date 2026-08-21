import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Импортируем наш роутер из файла handlers.py
from handlers import router

TOKEN = "8712827832:AAFRGUCcZBuOGBpw1BQC6tYnES7BTB5b85I"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


async def on_startup():
    print("\n" + "=" * 30)
    print("🚀 БОТ УСПЕШНО ЗАПУЩЕН И ГОТОВ К РАБОТЕ!")
    print("=" * 30 + "\n")


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.startup.register(on_startup)
    
    # Подключаем роутер с командами к диспетчеру
    dp.include_router(router)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())