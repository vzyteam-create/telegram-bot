from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv("8406040455:AAErPgkbH183hkLttTTgye_9S7MyOJtwi1M"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Бот запущен ✅")

if __name__ == "__main__":
    executor.start_polling(dp)
