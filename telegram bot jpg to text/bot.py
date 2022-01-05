import logging
import os
import shutil

import pathlib

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from imgTXT import imgTxt

import config

# log level
logging.basicConfig(level=logging.INFO)

# bot init
storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    img_sent = State()
    tiktok_leink_sent = State()


@dp.message_handler(commands=("imgtxt", "img_totxt"))
async def img_txt(message: types.Message, state: FSMContext):
    await message.answer("Отправьте изображение или отмените коммандой /cancel")
    await Form.img_sent.set()


# @dp.message_handler(commands=("ttsave"))
# async def tt_save_q(message: types.Message, state: FSMContext):
#     await message.answer("Отправьте ссылку на нужный тикток или отмените коммандой /cancel")
#     await Form.tiktok_keink_sent.set()
#
# @dp.message_handler(state=Form.img_sent)
# async def tt_save_s(message: types.Message, state: FSMContext):
#     link=message.text


@dp.message_handler(state=Form.img_sent, content_types=['photo'])
async def imgtxt_sent(message, state: FSMContext):
    await message.photo[-1].download('data/img.jpg')
    await message.answer("Полученный текст\n\n" + imgTxt("data/img.jpg"))
    await state.finish()


@dp.message_handler(state='*', commands=("cancel"))
async def img_txt(message: types.Message, state: FSMContext):
    await state.finish()


# комманда для чистки кеша
@dp.message_handler(commands="clc")
async def handle_docs_img(message):
    clear()
    await message.answer("Кэш потерт!")


# чистка
def clear():
    # shutil.rmtree('F:\\max\\Programs2\\Myfiles\\tgbot2\\data\\photos\\')
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
