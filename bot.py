from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import Command
from openai import AsyncOpenAI
import conf
from gpt import chat_answer

bot = Bot(token=conf.BOT_TOKEN)
dp = Dispatcher()
client = AsyncOpenAI(
    api_key=conf.API_KEY)


def start():
    print('Bot starting')


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    topic = await client.beta.threads.create()
    ids = topic.id
    response = "Представься, поздоровайся и расскажи что ты умеешь?"
    answer = await chat_answer(response, ids)
    await message.answer(answer)


@dp.message()
async def promt(message: types.Message):
    topic = await client.beta.threads.create()
    ids = topic.id
    response = message.text
    answer = await chat_answer(response, ids)
    await message.answer(answer)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    start()
    asyncio.run(main())

