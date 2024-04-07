import asyncio
import sys
import logging
from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder

def webAppBuilder() -> InlineKeyboardBuilder:
    builder =InlineKeyboardBuilder()
    builder.button(text="lest Go",web_app=WebAppInfo(url="https://vk.com/audios368978075"))
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply("Hi!",reply_markup=webAppBuilder())

async def main() -> None:
    bot = Bot('6277617045:AAHNTatUkNegioauk_tKPFrGx421xcS5_0Q', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

