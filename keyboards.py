from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Задание 1: Создание простого меню с кнопками
main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)


# Задание 2: Кнопки с URL-ссылками
inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url="https://lenta.ru/")],
   [InlineKeyboardButton(text="Музыка", url="https://rus.hitmotop.com/song/47828258")],
   [InlineKeyboardButton(text="Видео", url="https://rutube.ru/video/27c7f624a82578c408bc2de6701750ba/")]
])

# Задание 3: Динамическое изменение клавиатуры
inline_keyboard_test2 = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])

# Задание 3: Динамическое изменение клавиатуры
test = [("Опция 1", "option_1"), ("Опция 2", "option_2")]

async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key1, key2 in test:
       keyboard.add(InlineKeyboardButton(text=key1, callback_data=key2))
   return keyboard.adjust(2).as_markup()