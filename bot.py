
from aiogram import Dispatcher, Bot, types, executor
import requests
import json
from pprint import pprint as print
btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add("Do`llar -> So`m", "So`m -> Do`llar", "Rubl -> Do`llar", "Do`llar -> Rubl", "Rubl -> So`m", "So`m -> Rubl")

token = '2130953688:AAFmwi8Lp1z2EU-p6uAQVWaosBBkC4qWWdc'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def first(message: types.Message):
    await bot.send_message(message.chat.id, 'Salom, valyuta kurslarini bilishingiz uchun quyidagi tugmalardan birini bosing.', reply_markup=btn)

@dp.message_handler(content_types=['text'])
async def second(message: types.Message):
    url = 'https://v6.exchangerate-api.com/v6/e06e1270a84ce6eb8b4c162a/latest/'
    text = message.text
    sum = 'so`m'
    usd = 'do`llor'
    rub = 'rubl'
    if text == "Do`llar -> So`m":
        inputs = "USD"
        outputs = "UZS"

        response = requests.get(url+inputs)
        res = json.loads(response.text)
        result = res['conversion_rates'][outputs]
        await bot.send_message(message.chat.id, f"{result}  {sum}", reply_markup=btn)

    elif text == "So`m -> Do`llar":
        inputs = "UZS"
        outputs = "USD"

        response = requests.get(url + inputs)
        res = json.loads(response.text)
        result = res['conversion_rates'][outputs]
        await bot.send_message(message.chat.id, f"{result}  {usd}", reply_markup=btn)

    elif text == "Rubl -> Do`llar":
        inputs = "RUB"
        outputs = "USD"

        response = requests.get(url + inputs)
        res = json.loads(response.text)
        result = res['conversion_rates'][outputs]
        await bot.send_message(message.chat.id, f"{result}  {usd}", reply_markup=btn)

    elif text == "Do`llar -> Rubl":
        inputs = "USD"
        outputs = "RUB"

        response = requests.get(url + inputs)
        res = json.loads(response.text)
        result = res['conversion_rates'][outputs]
        await bot.send_message(message.chat.id, f"{result}  {rub}", reply_markup=btn)

    elif text == "Rubl -> So`m":
        inputs = "RUB"
        outputs = "UZS"

        response = requests.get(url + inputs)
        res = json.loads(response.text)
        result = res['conversion_rates'][outputs]
        await bot.send_message(message.chat.id, f"{result}  {sum}", reply_markup=btn)

    elif text == "So`m -> Rubl":
        inputs = "UZS"
        outputs = "RUB"

        response = requests.get(url + inputs)
        res = json.loads(response.text)
        result = res['conversion_rates'][outputs]
        await bot.send_message(message.chat.id, f"{result}  {rub}", reply_markup=btn)

    else:
        await bot.send_message(message.chat.id, '❌ Siz noto`g`ri ma`lumot kiritdingiz, tugmalardan birini tanlashingiz kerak!', reply_markup=btn)
    


if __name__ == '__main__':
    executor.start_polling(dp)
