from aiogram import Bot,Dispatcher,F,types
import asyncio
import logging
from aiogram.filters import Command


api = '7843091345:AAHdj6hMWA3JQWpeL4N50ixYIWlgKfeJpoY'
bot = Bot(api)
dp  =Dispatcher()


@dp.message(Command('start'))
async def send_hi(sms:types.Message):
    await sms.answer(text='Assalamu aleykum')




async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
