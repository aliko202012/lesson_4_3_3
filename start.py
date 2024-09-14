import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.handler import router
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

async def main():
    dp.include_router(router)  
    await dp.start_polling(bot) 
try:
    if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())  
except KeyboardInterrupt:
    print("exit")