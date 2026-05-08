from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("8734482130:AAGg_kg2l2qct3wvgMYm-YaR86vCFcSdt4M")  # Bot toekn
ADMINS = env.list("8426582765")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
