import asyncio
from asyncio import AbstractEventLoop,get_running_loop
from contextvars import Context
from logging import getLogger
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from main import start_message, help_message, echo_message
from aiogram.dispatcher import FSMContext
logger = getLogger(__name__)
bots = {}
#@angestrum

async def _start_bot(name: str, category_id: int) -> bool:
    callback = lambda: asyncio.create_task(start_bot(name, category_id))
    loop: AbstractEventLoop = get_running_loop()
    loop.call_soon(callback, context=Context())
    return True

async def start_bot(token,admin_id):
    storage = MemoryStorage()
    new_bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
    n_dp = Dispatcher(new_bot, storage=storage)
    bots[token] = n_dp
    bots['admin'] = admin_id
    try:
        await new_bot.send_message(admin_id,"<b>Bot ishga tushdi.</b>")
    except:
        pass
    n_dp.register_message_handler(start_message, commands='start')
    n_dp.register_message_handler(help_message, commands='help')
    n_dp.register_message_handler(echo_message)
    await n_dp.start_polling(timeout=10)

async def stop_bot(token):
    try:
        r_dp = bots[token]
        r_dp.stop_polling()
        await r_dp.wait_closed()
    except:
        pass