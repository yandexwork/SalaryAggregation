import logging
import json
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from models import Request, Response
from services import salary_service
from config import settings


dp = Dispatcher()


@dp.message()
async def message_handler(message: types.Message) -> None:
    request = Request(**json.loads(message.text))
    response: Response = await salary_service.get_salary_information(request.dt_from, request.dt_upto, request.group_type)
    await message.answer(str(response))


async def main() -> None:
    bot = Bot(settings.bot.token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
