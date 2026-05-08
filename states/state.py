from aiogram.dispatcher.filters.state import State,StatesGroup

class bottoken(StatesGroup):
    token = State()

class botstop(StatesGroup):
    token = State()