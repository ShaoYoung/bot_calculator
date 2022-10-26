from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
import logging
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv("TOKEN")


# есть описание через Ctrl
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('rat', rat_command))
app.add_handler(CommandHandler('comp', comp_command))


app.run_polling()