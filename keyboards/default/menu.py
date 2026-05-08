from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="🤖 Wikipedia bot yaratish")],
        [KeyboardButton(text="🗑 Botni o'chirish")]
    ],

    resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="@MistrUz"
)