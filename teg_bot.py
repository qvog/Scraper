from contextvars import Token
import json
from types import new_class
from aiogram import Bot, Dispatcher, executor, types
from config import toke

bot = Bot(token=toke)
dp = Dispatcher(bot)

@dp.message_handler(commands="all_news")

async def get_all_news(message: types.Message):
    with open ("new_dict.json") as file:
        news_dict = json.load(file)
    
    print(news_dict)

    for i, j in sorted(news_dict.items()):
        news = f"{j['get_discription']}\n" \
               f"{j['get_link']}\n"
        
        await message.answer(news)


def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()