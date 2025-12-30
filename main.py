import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("8406040455:AAErPgkbH183hkLttTTgye_9S7MyOJtwi1M")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Бот работает ✅")

async def on_startup(dp):
    await bot.delete_webhook(drop_pending_updates=True)
    print("Webhook удалён, бот запущен")

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
