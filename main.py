from aiogram import types
#@virtual_programmers_chanel
import wikipedia




async def start_message(message: types.Message):
    await message.answer(f"👋🏻 <b>Assalomu alaykum</b> {message.from_user.get_mention()}  <b>botimizga xush kelibsiz.</b>")


async def help_message(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))

wikipedia.set_lang('uz')
async def echo_message(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")