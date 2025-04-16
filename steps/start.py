from logger import logger
from telegram import Update
from telegram.ext import ContextTypes

from models.bot_steps import BotSteps

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("נמאס לך שאין לך תורים לספר? אני מטפל לך בזה. \n")
    await update.message.reply_text("נמאס לך לדבר? אתה יכול לשלוח /cancel בכל שלב ונעצור את השיחה.")
    await update.message.reply_text("אם אתה מבין את התנאים תשלח הודעה (כל הודעה)")

    return BotSteps.EMAIL.value
