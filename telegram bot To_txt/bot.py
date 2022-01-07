import logging
import os
import shutil
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from imgTXT import imgTxt
from tikok import tt_bot

import config

# log level
logging.basicConfig(level=logging.INFO)

# bot init
storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    img_sent = State()
    tiktok_link_sent = State()


@dp.message_handler(commands=["start"])
async def greetings(message: types.Message):
    start_buttons = ['/help']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Привет!\nДля "
                         "знакомства с функицоналом воспользуйтесь командой /help.",
                         reply_markup=keyboard)


@dp.message_handler(commands=("help"))
async def img_txt(message: types.Message):
    await message.answer("/imgtxt - Для перевода картинки в текст"
                         "\n/tiktoktxt - перевод 1 кадра тиктока в текст !ТОЛЬКО ССЫЛКИ С ПК ИЛИ БРАУЗЕРА!")


@dp.message_handler(commands=("imgtxt", "img_totxt"))
async def img_txt(message: types.Message, state: FSMContext):
    await message.answer("Отправьте изображение или отмените командой /cancel")
    await Form.img_sent.set()


@dp.message_handler(commands=("tiktoktxt"))
async def img_txt(message: types.Message, state: FSMContext):
    await message.answer("Отправьте ссылку на тикток с пк или отмените коммандой /cancel")
    await Form.tiktok_link_sent.set()


@dp.message_handler(state=Form.tiktok_link_sent, content_types=['text'])
async def imgtxt_sent(message, state: FSMContext):
    stt=tt_bot(message.text)
    if not stt== 'Некорректная ссылка!':
        await message.answer("Полученный текст\n\n" + imgTxt("data/tiktok/ttimg.jpg"))
    else:
        await message.answer(stt)
    await state.finish()


# img to text
@dp.message_handler(state=Form.img_sent, content_types=['text'])
async def imgtxt_senttxt(message, state: FSMContext):
    await message.answer("Отправьте изображение или отмените коммандой /cancel")


@dp.message_handler(state=Form.img_sent, content_types=['photo'])
async def imgtxt_sentimg(message, state: FSMContext):
    await message.photo[-1].download('data/img.jpg')
    await message.answer("Полученный текст\n\n" + imgTxt("data/img.jpg"))
    await state.finish()


@dp.message_handler(state='*', commands=("cancel"))
async def cancel(state: FSMContext):
    await state.finish()


# комманда для чистки кеша
@dp.message_handler(commands="clc")
async def clc(message):
    clear()
    await message.answer("Кэш потерт!")


# чистка
def clear():
    for root, dirs, files in os.walk('F:\\max\\Programs2\\Myfiles\\tgbot2\\data\\'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


def imgdownload(message):
    message.photo[-1].download('data/img.jpg')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
input()
