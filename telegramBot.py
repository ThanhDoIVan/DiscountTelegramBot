import json
from main import *

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink

bot = Bot(token=YOUR_TOKEN, parse_mode=types.ParseMode.HTML) 
# you can get your own token via BotFather at Telegram
dp = Dispatcher(bot)

async def bot_output(data, used_list, message: types.Message):
    count = 0
    n_count = 0
    for item in data:
        if item not in used_list:
            try:
                sizes = ', '.join(item.get('available_sizes'))
                card = f"{hlink(item.get('model_name'), item.get('link'))}\n" \
                       f"{hbold('Брэнд: ')} {item.get('brand_name')}\n" \
                       f"{hbold('Прайс: ')} {item.get('old_price')} BYN\n" \
                       f"{hbold('Доступные Размеры: ')} {sizes} \n" \
                       f"{hbold('Прайс со скидкой ')} -{item.get('discount')}%: {item.get('price')} BYN 🔥"
                used_list.append(item)
                await message.answer(card)
                count += 1
            except Exception as ex:
                print(f"{count} : {ex}")
            if count == 5:
                n_count = 0
                break
        else:
            n_count += 1

    if n_count >= 4:
        await message.answer('Вы достигли конца списка..')

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🧔 Мужское', '👩‍🦰 Женское']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Товары со скидкой 📈📉', reply_markup=keyboard)

@dp.message_handler(commands='menu')
async def menu(message: types.Message):
    await start(message)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer(f"🔸Выбирайте нужную вам категорию, и бот выдаст {hbold('5')} карточек раздела. \n"
                         "🔸Чтобы посмотреть новые предложения, повторно нажмите на нужную вам категорию. \n\n"
                         "🔸Чтобы выбрать другую категорию, напишите /start или /menu .")
    await message.answer('Пользуйтесь функциями бота и получайте удовольствие 🤓')

@dp.message_handler(Text(equals='🧔 Мужское'))
async def more_btn(message: types.Message):
    used_list = []
    buttons = ['Одежда "м"', 'Обувь "м"', 'Аксессуары "м"']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('Выберите тип товара 👔', reply_markup=keyboard)

    @dp.message_handler(Text(equals='Обувь "м"'))
    async def get_discount_man(message: types.Message):
        await message.answer('Please wait..')

        collect_data_men_shoes()

        with open('data/result_data_men_shoes.json', encoding='utf-8') as file:
            data = json.load(file)

        await bot_output(data, used_list, message)


    @dp.message_handler(Text(equals='Одежда "м"'))
    async def more_btn(message: types.Message):
        buttons = ['Верхняя одежда', 'Свитеры', 'Толстовки', 'Штаны', 'Рубашки']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*buttons)

        await message.answer('Выберите категорию 🥼👕👖', reply_markup=keyboard)


        @dp.message_handler(Text(equals='Верхняя одежда'))
        async def get_discount_man(message: types.Message):
            await message.answer('Please wait..')

            collect_data_men_outerwear()

            with open('data/result_data_men_outerwear.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Свитеры'))
        async def get_discount_man(message: types.Message):
            await message.answer('Please wait..')

            collect_data_men_pullover()

            with open('data/result_data_men_pullover.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Толстовки'))
        async def get_discount_man(message: types.Message):
            await message.answer('Please wait..')

            collect_data_men_sweatshirts()

            with open('data/result_data_men_sweatshirts.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Штаны'))
        async def get_discount_man(message: types.Message):
            await message.answer('Please wait..')

            collect_data_men_pants()

            with open('data/result_data_men_pants.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Рубашки'))
        async def get_discount_man(message: types.Message):
            await message.answer('Please wait..')

            collect_data_men_shirts()

            with open('data/result_data_men_shirts.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)


    @dp.message_handler(Text(equals='Аксессуары "м"'))
    async def get_discount_man(message: types.Message):
        await message.answer('Please wait..')

        collect_data_men_accessories()

        with open('data/result_data_men_accessories.json', encoding='utf-8') as file:
            data = json.load(file)

        await bot_output(data, used_list, message)

@dp.message_handler(Text(equals='👩‍🦰 Женское'))
async def more_btn(message: types.Message):
    used_list = []
    buttons = ['Одежда "ж"', 'Обувь "ж"', 'Аксессуары "ж"']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('Выберите тип товара 👗', reply_markup=keyboard)

    @dp.message_handler(Text(equals='Обувь "ж"'))
    async def get_discount_woman(message: types.Message):
        await message.answer('Please wait..')

        collect_data_women_shoes()

        with open('data/result_data_women_shoes.json', encoding='utf-8') as file:
            data = json.load(file)

        await bot_output(data, used_list, message)


    @dp.message_handler(Text(equals='Одежда "ж"'))
    async def more_btns(message: types.Message):
        buttons = ['Футболки и Поло', 'Комбинезоны', 'Платья', 'Свитшоты и Худи', 'Брюки']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*buttons)

        await message.answer('Выберите категорию 🥻👘👚', reply_markup=keyboard)

        @dp.message_handler(Text(equals='Футболки и Поло'))
        async def get_discount_woman(message: types.Message):
            await message.answer('Please wait..')

            collect_data_women_shirts()

            with open('data/result_data_women_shirts.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Комбинезоны'))
        async def get_discount_woman(message: types.Message):
            await message.answer('Please wait..')

            collect_data_women_overalls()

            with open('data/result_data_women_overalls.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Платья'))
        async def get_discount_woman(message: types.Message):
            await message.answer('Please wait..')

            collect_data_women_dress()

            with open('data/result_data_women_dress.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Свитшоты и Худи'))
        async def get_discount_woman(message: types.Message):
            await message.answer('Please wait..')

            collect_data_women_hoodies()

            with open('data/result_data_women_hoodies.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)

        @dp.message_handler(Text(equals='Брюки'))
        async def get_discount_woman(message: types.Message):
            await message.answer('Please wait..')

            collect_data_women_trousers()

            with open('data/result_data_women_trousers.json', encoding='utf-8') as file:
                data = json.load(file)

            await bot_output(data, used_list, message)


    @dp.message_handler(Text(equals='Аксессуары "ж"'))
    async def get_discount_woman(message: types.Message):
        await message.answer('Please wait..')

        collect_data_women_accessories()

        with open('data/result_data_women_accessories.json', encoding='utf-8') as file:
            data = json.load(file)

        await bot_output(data, used_list, message)

def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
