import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

import config
from parsingCPR import parse_crypto_rub, parse_crypto_usd, cr_best_up, cr_best_down
from parsingSTCK import parse_usd_up, parse_usd_dwn, parse_usd_top, parse_rub_top, parse_rub_up, parse_rub_down

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def greetings(message: types.Message):
    start_buttons = ['/🆓Крипта', '/💲USA(XAX)', '/🇷🇺RUS(MOEX)']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Привет!\nДанный бот предназначен для быстрого получения актульной сводки по рынкам.\nДля "
                         "знакомства с функицоналом воспользуйтесь командой /help или меню комманд.",
                         reply_markup=keyboard)


@dp.message_handler(commands=["help"])
async def Help(message: types.Message):
    start_buttons = ['/🆓Крипта', '/💲USA(XAX)', '/🇷🇺RUS(MOEX)']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Функционал бота:\n"
                         "\n🆓 Крпитовалюта:\n/crypto_RUB - Сводка по актуальной криптовалюте в рублях\n/crypto_USD - "
                         "Сводка по актуальной криптовалюте в долларах\n"
                         "/crypto_up - Лидер роста в процентном соотношении за 24 часа среди акутальных криптовалют\n"
                         "/crypto_down - Сильнейшие падения в процентном соотношении за 24 часа среди акутальных криптовалют"
                         "\n\n💲 Американская биржа:"
                         "\n/Usa_top - 10 cамых популярных акций в США"
                         "\n/Usa_up - Лидеры роста на америкаснкой бирже за 24 часа"
                         "\n/Usa_down - Сильнейшие падения на америкаснкой бирже за 24 часа"
                         "\n\n🇷🇺 Русская биржа (MOEX):"
                         "\n/ru_top - 10 cамых популярных акций в РФ (MOEX)"
                         "\n/ru_up - Лидеры роста на MOEX бирже за 24 часа"
                         "\n/ru_down - Сильнейшие падения на MOEX бирже за 24 часа")


@dp.message_handler(commands=("crypto", "🆓Крипта"))
async def CRP(message: types.Message):
    await message.answer('\n🆓 Крпитовалюта:\n/crypto_RUB - Сводка по актуальной криптовалюте в рублях\n/crypto_USD - '
                         'Сводка по актуальной криптовалюте в долларах\n'
                         '/crypto_up - Лидер роста в процентном соотношении за 24 часа среди акутальных криптовалют\n'
                         '/crypto_down - Сильнейшие падения в процентном соотношении за 24 часа среди акутальных '
                         'криптовалют')


@dp.message_handler(commands=("usa","/💲USA(XAX)"))
async def US(message: types.Message):
    await message.answer("\n\n🇺🇸 Американская биржа:"
                         "\n/Usa_top - 10 cамых популярных акций в США"
                         "\n/Usa_up - Лидеры роста на америкаснкой бирже за 24 часа"
                         "\n/Usa_down - Сильнейшие падения на америкаснкой бирже за 24 часа")


@dp.message_handler(commands=("ru","🇷🇺RUS(MOEX)"))
async def RUS(message: types.Message):
    await message.answer("\n\n💲 Русская биржа (MOEX):"
                         "\n/ru_top - 10 cамых популярных акций в РФ (MOEX)"
                         "\n/ru_up - Лидеры роста на MOEX бирже за 24 часа"
                         "\n/ru_down - Сильнейшие падения на MOEX бирже за 24 часа")


@dp.message_handler(commands=("крипта", "crypto_RUB", "cryptorub"))
async def crRu(message: types.Message):
    await message.answer(parse_crypto_rub())


@dp.message_handler(commands=("cryptotop", "crypto_USD", "cryptousd"))
async def crUS(message: types.Message):
    await message.answer(parse_crypto_usd())


@dp.message_handler(commands=("crup", "crypto_up"))
async def crUp(message: types.Message):
    await message.answer("Лидер роста среди акутальных криптовалют:\n" + cr_best_up())


@dp.message_handler(commands=("crdown", "crypto_down"))
async def crDw(message: types.Message):
    await message.answer("Сильнейшее падение среди акутальных криптовалют:\n" + cr_best_down())


@dp.message_handler(commands=("usaup", "Usa_up"))
async def usSTUp(message: types.Message):
    await message.answer("Лидеры роста в США:\n" + parse_usd_up())


@dp.message_handler(commands=("usadwn", "Usa_down"))
async def usSTdwn(message: types.Message):
    await message.answer("Лидеры падения в США:\n" + parse_usd_dwn())


@dp.message_handler(commands=("usatop", "Usa_top"))
async def usSTdwn(message: types.Message):
    await message.answer("10 cамых популярных акций в США:\n" + parse_usd_top())


@dp.message_handler(commands=("rutop", "ru_top"))
async def rutop(message: types.Message):
    await message.answer("10 cамых популярных акций в РФ:\n" + parse_rub_top())


@dp.message_handler(commands=("rudown", "ru_down"))
async def rutop(message: types.Message):
    await message.answer("Лидеры падения в РФ:\n" + parse_rub_down())


@dp.message_handler(commands=("ruup", "ru_up"))
async def rutop(message: types.Message):
    await message.answer("Лидеры роста в РФ:\n" + parse_rub_up())


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
input()
