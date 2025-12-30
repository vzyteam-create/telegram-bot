from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv("8514866233:AAG6SYtXYkfkB3k5FUtVFLZDMgsYKiPbYKY"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Бот запущен ✅")

if __name__ == "__main__":
    executor.start_polling(dp)
