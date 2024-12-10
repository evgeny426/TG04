import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
   await callback.answer("Новости подгружаются", show_alert=True)
   await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.test_keyboard())

# Задание 1: Создание простого меню с кнопками
@dp.message(F.text == "Привет")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!')

# Задание 1: Создание простого меню с кнопками
@dp.message(F.text == "Пока")
async def test_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}!')

# Задание 1: Создание простого меню с кнопками
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb.main)

# Задание 2: Кнопки с URL-ссылками
@dp.message(Command('links'))
async def links_command(message: Message):
   await message.answer('Выберите действие:', reply_markup=kb.inline_keyboard_test)

# Задание 3: Динамическое изменение клавиатуры
@dp.message(Command('dynamic'))
async def dynamic_command(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb.inline_keyboard_test2)

# Задание 3: Динамическое изменение клавиатуры
@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
   await callback.message.edit_text('Выберите:', reply_markup=await kb.test_keyboard())

# Задание 3: Динамическое изменение клавиатуры
@dp.callback_query(F.data == 'option_1')
async def option1(callback: CallbackQuery):
    await callback.answer('Вы выбрали Опцию 1!')
    await callback.message.answer('Это сообщение для Опции 1.')

# Задание 3: Динамическое изменение клавиатуры
@dp.callback_query(F.data == 'option_2')
async def option1(callback: CallbackQuery):
    await callback.answer('Вы выбрали Опцию 2!')
    await callback.message.answer('Это сообщение для Опции 2.')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())