from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from loader import dp, bot, db
from multi import start_bot,stop_bot,_start_bot
from states.state import bottoken,botstop

@dp.message_handler(text="🤖 Wikipedia bot yaratish",state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.update_data({"tuman_id": "Wiki"})
    await message.answer("Bot tokenini kiriting... bot tokenini @BotFather dan oling")
    await bottoken.token.set()

@dp.message_handler(state=bottoken.token)
async def bot_echo(message: types.Message,state:FSMContext):
    await state.update_data({"tok": "Wiki"})
    malumot = await state.get_data()
    wiki =  malumot.get('tuman_id')
    tok = malumot.get('tok')
    if db.select_user(token=message.text):
        await message.answer("Kechirasiz siz Avvalroq bu bot tokenini ishlatganisz va bu botingiz ishlab turibdi.")
        await state.finish()
    else:
        try:
            n_bot = Bot(token=message.text)
            bb = await n_bot.get_me()
            try:
                db.add_user(Name=wiki,Token=message.text)
            except:
                pass
            xabar = await bot.send_message(chat_id=message.from_user.id,text=f"Tayorlanmoqda...")
            for x in range(1,11):
                text0=x*10
                text1 =x*'⬛️'
                text2 =(10-x)*'⬜️'
                await xabar.edit_text(f"{text0}%\n{text1}{text2}")
            await xabar.delete()
            await bot.send_message(chat_id=message.from_user.id, text=f"Bot ishga tushdi... @{bb.username}")
            await state.finish()
            await _start_bot(message.text,message.from_user.id)
            # await start_bot(message.text,message.from_user.id)

        except:
            await bot.send_message(chat_id=message.from_user.id, text=f"Qandaydir xatolik yuzaga keldi qayta urining yoki tokenni tekshiring...")
            await state.finish()



@dp.message_handler(text="🗑 Botni o'chirish",state='*')
async def bot_echo(message: types.Message):
    await message.answer("Bot Tokenini kiriting...")
    await botstop.token.set()

@dp.message_handler(state=botstop.token)
async def bot_echo(message: types.Message, state: FSMContext):
    if db.select_user(token=message.text):
        try:
            db.delete_users(Token=str(message.text))
            await stop_bot(token=message.text)
        except:
            pass
        await message.answer("Bot o'chirildi...")
        await state.finish()
    else:
        await message.answer("Kechirasiz bunday token mavjud emas... yoki bu token orqalik bizdan bot ochilmagan.")
        await state.finish()

